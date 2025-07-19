import subprocess

def run_subfinder(target):
    try:
        print(f"[+] Running Subfinder on {target}...")
        result = subprocess.run(["subfinder", "-d", target, "-silent"], capture_output=True, text=True)
        print(result.stdout)
        return result.stdout.splitlines()
    except Exception as e:
        print(f"[-] Subfinder failed: {e}")
        return []
