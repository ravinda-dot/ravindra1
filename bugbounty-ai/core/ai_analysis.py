# Placeholder for ai_analysis.py
from ai_models import bug_explainer, severity_predictor, poc_generator
import os
import json

def run_analysis(scan_results):
    print("\n🧠 Running AI Analysis...")

    for tool, result_path in scan_results.items():
        if not os.path.exists(result_path):
            continue

        with open(result_path, 'r') as f:
            lines = f.readlines()

        for idx, line in enumerate(lines):
            print(f"\n🔍 Analyzing finding from {tool} #{idx+1}")
            finding = line.strip()

            explanation = bug_explainer.explain(finding)
            severity = severity_predictor.predict(finding)
            poc = poc_generator.generate(finding)

            print(f"📌 Bug: {finding}")
            print(f"🧾 Explanation: {explanation}")
            print(f"🔥 Severity: {severity}")
            print(f"🧪 PoC: {poc}")
