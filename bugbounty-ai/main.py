import os
import re
from modules.recon.subdomain import run_subfinder
from modules.recon.portscan import run_naabu
from modules.recon.http_probe import run_httpx
from modules.vuln.xss_scan import run_dalfox
from modules.vuln.sqli_scan import run_sqlmap
from modules.vuln.template_scan import run_nuclei
from modules.utils.reporter import generate_report
from modules.utils.ai_analysis import analyze_with_ai


def banner():
    print("=" * 60)
    print("        🔍 AI Bug Bounty Automation Tool - Start Hunting")
    print("=" * 60)


def clean_target_url(input_url):
    """Cleans input like https://example.com to example.com"""
    domain = re.sub(r"https?://", "", input_url)
    return domain.strip("/")


def main():
    banner()
    raw_input = input("Enter the target domain (e.g., example.com): ").strip()
    target = clean_target_url(raw_input)

    # 1. Subdomain Enumeration
    try:
        subdomains = run_subfinder(target) or []
    except Exception as e:
        print(f"[-] Subfinder failed: {e}")
        subdomains = []

    # 2. HTTP Probing
    try:
        live_hosts = run_httpx(subdomains) or []
    except Exception as e:
        print(f"[-] Httpx failed: {e}")
        live_hosts = []

    # 3. Port Scanning
    try:
        ports = run_naabu(live_hosts) or []
    except Exception as e:
        print(f"[-] Naabu failed: {e}")
        ports = []

    # 4. Vulnerability Scanning
    try:
        xss_results = run_dalfox(live_hosts) or []
    except Exception as e:
        print(f"[-] Dalfox failed: {e}")
        xss_results = []

    try:
        sqli_results = run_sqlmap(live_hosts) or []
    except Exception as e:
        print(f"[-] SQLMap failed: {e}")
        sqli_results = []

    try:
        nuclei_results = run_nuclei(live_hosts) or []
    except Exception as e:
        print(f"[-] Nuclei failed: {e}")
        nuclei_results = []

    # 5. AI-based Analysis
    try:
        all_results = xss_results + sqli_results + nuclei_results
        ai_summary = analyze_with_ai(all_results)
    except Exception as e:
        print(f"[-] AI analysis failed: {e}")
        ai_summary = "No AI summary available."

    # 6. Report Generation
    try:
        findings = {
            "subdomains": subdomains,
            "live_hosts": live_hosts,
            "vulnerabilities": all_results
        }
        safe_target = re.sub(r'[^\w\-_]', '_', target)
        generate_report(safe_target, findings, ai_summary)
        print("\n✅ Done! Report generated in /output directory.")
    except Exception as e:
        print(f"[-] Report generation failed: {e}")


if __name__ == "__main__":
    main()
