# Placeholder for subfinder_wrapper.py
import subprocess
import os

def run_subfinder(domain):
    print(f"[+] Running Subfinder on: {domain}")
    output_file = f"data/subdomains/{domain}_subdomains.txt"
    os.makedirs("data/subdomains", exist_ok=True)

    try:
        subprocess.run(
            ["subfinder", "-d", domain, "-silent", "-o", output_file],
            check=True
        )
        with open(output_file, "r") as f:
            subdomains = [line.strip() for line in f.readlines() if line.strip()]
        print(f"[✓] Found {len(subdomains)} subdomains.")
        return subdomains

    except subprocess.CalledProcessError:
        print("[!] Subfinder failed.")
        return []
