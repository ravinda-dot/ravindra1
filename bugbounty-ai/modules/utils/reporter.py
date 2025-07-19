import os
import json

import datetime
...
timestamp = datetime.datetime.now()

def generate_report(target, findings, ai_summary):

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)

    safe_target = target.replace("https://", "").replace("http://", "").replace(".", "_").replace("/", "")
    report_path = os.path.join(output_dir, f"report_{safe_target}.txt")

    with open(report_path, "w", encoding="utf-8") as report_file:
        report_file.write(f"Bug Bounty AI Report for {safe_target}\n")
        report_file.write("=" * 50 + "\n\n")

        report_file.write("Subdomains Found:\n")
        report_file.write("\n".join(findings.get("subdomains", [])) + "\n\n")

        report_file.write("Live Hosts:\n")
        report_file.write("\n".join(findings.get("live_hosts", [])) + "\n\n")

        report_file.write("Vulnerabilities Found:\n")
        for item in findings.get("vulnerabilities", []):
            report_file.write(f"- {item}\n")

        report_file.write("\nAI Summary:\n")
        report_file.write(ai_summary.strip() if ai_summary else "No AI summary available.")

        report_file.write(f"\n\nGenerated at: {datetime.datetime.now()}\n")
