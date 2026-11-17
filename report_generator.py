
import json
from datetime import datetime

def generate_report(results):

    report = {
        "project": "Smart Compliance Checker",
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_requirements": len(results),
        "passed": sum(1 for status in results.values() if status == "PASS"),
        "failed": sum(1 for status in results.values() if status == "FAIL"),
        "results": results
    }

    with open("compliance_report.json", "w") as file:
        json.dump(report, file, indent=4)

    print("\nCompliance report generated successfully!")
