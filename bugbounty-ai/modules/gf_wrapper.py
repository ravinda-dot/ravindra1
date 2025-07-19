# Placeholder for gf_wrapper.py
import subprocess
import os

def run_gf_patterns(domain, input_file):
    print(f"[+] Running gf patterns on {input_file}")
    os.makedirs("data/params", exist_ok=True)
    output_file = f"data/params/{domain}_gf.txt"

    try:
        with open(output_file, "w") as out:
            subprocess.run(["gf", "xss"], stdin=open(input_file), stdout=out, check=True)
        print("[✓] gf xss patterns extracted.")
        return output_file
    except subprocess.CalledProcessError:
        print("[!] gf failed.")
        return None
