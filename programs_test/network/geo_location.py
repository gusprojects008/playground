import requests
import json

ip_input = input("type it ip:")
def location_ip(ip):
    get_info = requests.get(f"https://ipinfo.io/{ip}/json")
    print(get_info.text)
    json_format = json.loads(get_info.text)
    info_full = f"{json_format['city']}\n{json_format['region']}\n{json_format['country']}\n{json_format['loc']}\n{json_format['org']}\n{json_format['postal']}\n{json_format['timezone']}"
    print(info_full)

location_ip(ip_input)
