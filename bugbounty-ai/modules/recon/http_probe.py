import subprocess

def run_httpx(targets):
    alive_domains = []
    print("[+] Probing for alive domains using httpx...")
    try:
        process = subprocess.Popen(['httpx', '-silent'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        stdout, _ = process.communicate('\n'.join(targets))
        alive_domains = stdout.splitlines()
        for domain in alive_domains:
            print(f"    [+] Alive: {domain}")
    except Exception as e:
        print(f"[-] Error running httpx: {e}")
    return alive_domains
