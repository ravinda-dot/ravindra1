# Placeholder for nuclei_wrapper.py
import subprocess
import os

def run_nuclei(domain, input_file):
    print(f"[+] Running Nuclei on subdomains")
    os.makedirs("data/results", exist_ok=True)
    output_file = f"data/results/{domain}_nuclei.txt"

    try:
        subprocess.run(["nuclei", "-l", input_file, "-o", output_file], check=True)
        print("[✓] Nuclei scan complete.")
        return output_file
    except subprocess.CalledProcessError:
        print("[!] Nuclei scan failed.")
        return None
