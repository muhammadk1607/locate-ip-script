import argparse
import csv
import os
from functools import lru_cache

import ipinfo
from colorama import Fore, Style
from colorama import init as colorama_init

colorama_init()

# Read CSV file, parse it's columns (id, name, email, ip)
# Lookup location for IP address and add it to the row
# Write the new row to a new CSV file

IPINFO_HANDLER = ipinfo.getHandler(os.getenv("IPINFO_TOKEN"))


def read_csv(file_path):
    with open(file_path, mode="r", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]

    if not data:
        print(f"❌ {Fore.RED}No data found in {file_path}{Style.RESET_ALL}")
        return []

    return data


def write_csv(file_path, data):
    with open(file_path, mode="w", newline="", encoding="utf-8") as csvfile:
        fieldnames = data[0].keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


@lru_cache(maxsize=None)
def lookup_ip_location(ip):
    print(f"Looking up location for IP: {ip}")
    details = IPINFO_HANDLER.getDetails(ip)

    return details.city


def process_csv(input_file, output_file):
    data = read_csv(input_file)
    for row in data:
        ip = row.get("ip")
        if ip:
            location = lookup_ip_location(ip)
            row["location"] = location
        else:
            row["location"] = "IP not found"
    write_csv(output_file, data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Process a CSV file with IP addresses."
    )
    parser.add_argument(
        "-i",
        "--input",
        type=str,
        default="input.csv",
        help="Input CSV file path (default: input.csv)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        default="output.csv",
        help="Output CSV file path (default: output.csv)",
    )
    args = parser.parse_args()
    process_csv(args.input, args.output)
    print(
        f"✅ {Fore.GREEN}Processed {args.input} and saved to {args.output}{Style.RESET_ALL}"
    )
