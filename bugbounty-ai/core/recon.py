# Placeholder for recon.py
import os
from modules import subfinder_wrapper, arjun_wrapper, gf_wrapper

def recon(domain):
    print(f"\n[🔍] Starting Recon for {domain}")
    subdomains_file = subfinder_wrapper.run_subfinder(domain)

    if not subdomains_file or not os.path.exists(subdomains_file):
        print("[!] Subdomain enumeration failed.")
        return

    # You can customize this to collect wayback URLs or paramspider too later
    # Now, Arjun runs on subdomain URLs (optional)
    arjun_wrapper.run_arjun(domain, subdomains_file)

    # Apply gf patterns
    gf_output = gf_wrapper.run_gf_patterns(domain, subdomains_file)
    if not gf_output:
        print("[!] No URLs found for further scanning.")

    print(f"[🏁] Recon Completed for {domain}")
    return {
        "subdomains": subdomains_file,
        "gf_output": gf_output
    }
