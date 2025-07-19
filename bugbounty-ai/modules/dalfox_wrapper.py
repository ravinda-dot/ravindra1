# Placeholder for dalfox_wrapper.py
import subprocess
import os

def run_dalfox(domain, input_file):
    print(f"[+] Running Dalfox on filtered URLs")
    os.makedirs("data/results", exist_ok=True)
    output_file = f"data/results/{domain}_dalfox.txt"

    try:
        with open(output_file, "w") as out:
            subprocess.run(["dalfox", "file", input_file, "--output", output_file], check=True)
        print("[✓] Dalfox scan complete.")
        return output_file
    except subprocess.CalledProcessError:
        print("[!] Dalfox scan failed.")
        return None
