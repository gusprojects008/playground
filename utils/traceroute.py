#!/usr/bin/env python3

from scapy.all import IP, TCP, sr1, traceroute, conf
import argparse
import socket
import sys
try:
    import requests
except:
    requests = None

def resolve_hostname(ip: str) -> str | None:
    try:
        name = socket.gethostbyaddr(ip)[0]
        return name
    except socket.herror:
        return None
    except Exception:
        return None

def ipinfo_lookup(ip: str, timeout: int = 5) -> dict | None:
    if requests is None:
        return None
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json", timeout=timeout)
        if r.status_code == 200:
            return r.json()
        return None
    except Exception:
        return None


def send_probe_tcp(target: str, dport: int, timeout: int = 5):
    packet = IP(dst=target) / TCP(dport=dport, flags="S")
    try:
        response = sr1(packet, timeout=timeout, verbose=0)
        return response
    except PermissionError:
        print("[!] Permission denied: run with sudo/root to send packets.")
        return None
    except Exception:
        print(f"[!] Error sending TCP probe. {error}")
        return None

def do_traceroute(target: str, dport: int, maxttl: int, timeout: int = 5):
    try:
        response, unanswered = traceroute(target, dport=dport, maxttl=maxttl, timeout=timeout, verbose=0)
        return response, unanswered
    except PermissionError:
        print("[!] Permission denied: run with sudo/root to send packets.")
        return None, None
    except Exception as error:
        print(f"[!] Error running traceroute: {error}")
        return None, None

def print_ip_info(ip: str, show_location: bool, ipinfo_timeout: int = 5):
    hostname = resolve_hostname(ip)
    if hostname:
        print(f"    Hostname: {hostname}")
    else:
        print("    Hostname: (not found)")

    if show_location:
        info = ipinfo_lookup(ip, timeout=ipinfo_timeout)
        if info:
            city = info.get("city", "")
            region = info.get("region", "")
            country = info.get("country", "")
            loc = info.get("loc", "")
            org = info.get("org", "")
            postal = info.get("postal", "")
            timezone = info.get("timezone", "")
            print("    Location info:")
            print(f"      - City:    {city}")
            print(f"      - Region:  {region}")
            print(f"      - Country: {country}")
            print(f"      - Loc:     {loc}")
            print(f"      - Org:     {org}")
            print(f"      - Postal:  {postal}")
            print(f"      - TZ:      {timezone}")
        else:
            if requests is None:
                print("    Location info: (requests not installed)")
            else:
                print("    Location info: (not available / request failed)")


def main():
    parser = argparse.ArgumentParser(description="Simple traceroute helper using Scapy")
    parser.add_argument("-i", "--iface", required=True, help="Network interface to use")
    parser.add_argument("--target", required=True, help="Target IP or hostname to trace")
    parser.add_argument("-p", "--port", type=int, default=33434,
                        help="Destination port for probes (default: 33434)")
    parser.add_argument("--ttl", type=int, default=30, help="Max TTL / hops (default: 30)")
    parser.add_argument("--timeout", type=int, default=5, help="Timeout per probe in seconds (default: 5)")
    parser.add_argument("--no-location", action="store_true",
                        help="Skip ipinfo.io lookups (faster / offline-friendly)")
    parser.add_argument("--no-initial-probe", action="store_true",
                        help="Skip initial TCP SYN probe (only run traceroute)")
    args = parser.parse_args()

    target = args.target
    dport = args.port
    iface = args.iface
    if iface:
        conf.iface = iface
    maxttl = args.ttl
    timeout = args.timeout
    show_location = not args.no_location
    do_initial = not args.no_initial_probe

    print(f"[+] Target: {target}")
    print(f"[+] Port:   {dport}")
    if iface:
        print(f"[+] Interface: {iface}")
    print(f"[+] Max TTL: {maxttl}")
    print(f"[+] Timeout: {timeout}s")
    print()

    if do_initial:
        print("[*] Sending initial TCP SYN probe...")
        response = send_probe_tcp(target, dport, timeout=timeout)
        if response:
            print("[+] Response to TCP SYN probe:")
            print(f"    - From: {response.src}")
            print(f"    - Summary: {response.summary()}")
            print_ip_info(response.src, show_location, ipinfo_timeout=timeout)
        else:
            print("[!] No response to TCP SYN probe (or probe failed).")
        print()

    print("[*] Running traceroute (UDP/ICMP via Scapy)...")

    response, unanswered = do_traceroute(target, dport, maxttl, timeout=timeout)

    if response is None:
        print("[!] Traceroute failed.")
        sys.exit(1)

    print("\n[+] Traceroute results (per hop):")

    try:
        for snd, rcv in response:
            if rcv is None:
                print(f" - No response for probe: {snd.summary()}")
                continue
            hop_ip = rcv.src
            ttl_used = snd.ttl if hasattr(snd, "ttl") else "?"
            print(f" - Hop (ttl={ttl_used}) -> {hop_ip} | {rcv.summary()}")
            print_ip_info(hop_ip, show_location, ipinfo_timeout=timeout)
    except Exception:
        print("[!] Unexpected traceroute result format; dumping summary:")
        print(response.summary())

    print("\n[+] Unanswered probes (if any):")
    if unanswered:
        try:
            for packet in unanswered:
                print(f" - {packet.summary()}")
        except Exception:
            print(" - (could not iterate unanswered list)")
    else:
        print(" - (none)")

    print("\n[+] Done.\n")


if __name__ == "__main__":
    conf.verb = 1
    main()
