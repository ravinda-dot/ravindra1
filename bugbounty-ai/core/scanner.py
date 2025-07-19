# Placeholder for scanner.py
import os
from modules import dalfox_wrapper, nuclei_wrapper

def scan(domain, recon_output):
    print(f"\n[🚨] Starting Scanning for {domain}")
    results = {}

    if recon_output.get("gf_output"):
        dalfox_result = dalfox_wrapper.run_dalfox(domain, recon_output["gf_output"])
        results["dalfox"] = dalfox_result

    if recon_output.get("subdomains"):
        nuclei_result = nuclei_wrapper.run_nuclei(domain, recon_output["subdomains"])
        results["nuclei"] = nuclei_result

    print(f"[✅] Scanning Completed for {domain}")
    return results
