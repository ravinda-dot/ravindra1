# Placeholder for arjun_wrapper.py
import subprocess
import os

def run_arjun(domain, input_file):
    print(f"[+] Running Arjun on target URLs")
    os.makedirs("data/params", exist_ok=True)
    output_file = f"data/params/{domain}_arjun.txt"

    try:
        subprocess.run(["arjun", "-i", input_file, "-o", output_file], check=True)
        print("[✓] Arjun parameter discovery complete.")
        return output_file
    except subprocess.CalledProcessError:
        print("[!] Arjun failed.")
        return None
