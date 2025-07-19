# modules/utils/ai_analysis.py
def analyze_with_ai(findings: list) -> str:
    analysis = "AI Summary Report:\n"
    for finding in findings:
        analysis += f"- {finding['title']}: {finding['description']}\n"
    return analysis
