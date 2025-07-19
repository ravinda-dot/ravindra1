import subprocess

def run_nuclei(urls):
    print("[+] Starting template scan using nuclei...")
    for url in urls:
        print(f"    [+] Scanning {url}")
        try:
            subprocess.run(["nuclei", "-u", url, "-t", "cves/", "-severity", "high,critical"], check=True)
        except Exception as e:
            print(f"[-] Nuclei scan failed for {url}: {e}")
