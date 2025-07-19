import subprocess

def run_sqlmap(urls):
    print("[+] Starting SQL Injection scan using sqlmap...")
    for url in urls:
        print(f"    [+] Scanning {url}")
        try:
            subprocess.run(["sqlmap", "-u", url, "--batch", "--level=2"], check=True)
        except Exception as e:
            print(f"[-] SQLMap scan failed for {url}: {e}")
