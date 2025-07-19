import subprocess

def run_naabu(target):
    try:
        print(f"[+] Running Naabu on {target}...")
        result = subprocess.run(["naabu", "-host", target, "-silent"], capture_output=True, text=True)
        print(result.stdout)
        return result.stdout.splitlines()
    except Exception as e:
        print(f"[-] Naabu failed: {e}")
        return []
