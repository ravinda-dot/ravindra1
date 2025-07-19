import subprocess

def run_dalfox(domains):
    print("[+] Starting XSS scan using Dalfox...")
    try:
        for domain in domains:
            print(f"    [+] Scanning {domain}")
            subprocess.run(["dalfox", "url", domain], check=True)
    except Exception as e:
        print(f"[-] Error running Dalfox: {e}")
