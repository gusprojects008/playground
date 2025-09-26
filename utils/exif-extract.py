#!/usr/bin/env python3

import argparse
import subprocess
import sys
from pathlib import Path


def run_tool(cmd, description):
    try:
        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            check=True
        )
        return f"\n=== {description} ===\n{result.stdout}\n"
    except FileNotFoundError:
        return f"\n=== {description} ===\n[!] Tool not found: {cmd[0]}\n"
    except subprocess.CalledProcessError as e:
        return f"\n=== {description} ===\n[!] Error running {cmd[0]}: {e}\n"
    except Exception as e:
        return f"\n=== {description} ===\n[!] Unexpected error: {e}\n"


def extract_img(path: Path, output: Path):
    sections = []
    sections.append(run_tool(["exiftool", "-v", str(path)], "Exiftool (metadata)"))
    sections.append(run_tool(["binwalk", "-v", str(path)], "Binwalk (file analysis)"))
    sections.append(run_tool(["strings", str(path)], "Strings (printable content)"))
    sections.append(run_tool(["xxd", "-a", str(path)], "Hexdump (xxd)"))

    with open(output, "w", encoding="utf-8") as f:
        for sec in sections:
            f.write(sec)

    print(f"[+] Analysis complete. Results saved in: {output}")


def main():
    parser = argparse.ArgumentParser(
        description="Extract metadata and hidden data from image files using exiftool, binwalk, strings, and xxd."
    )
    parser.add_argument("--path", type=Path, required=True, help="Path to the image file to analyze")
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("./exif-extract-result.txt"),
        help="Output file to save the analysis (default: exif-extract-result.txt)"
    )

    args = parser.parse_args()

    if not args.path.exists():
        print(f"[!] File not found: {args.path}")
        sys.exit(1)

    extract_img(args.path, args.output)


if __name__ == "__main__":
    main()
