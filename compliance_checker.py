
import PyPDF2
import re
from report_generator import generate_report

# Compliance requirements from sample.pdf
requirements = [
    "All documents must be processed through the central ingestion engine.",
    "Data extraction must maintain 100% character accuracy.",
    "Automated logs are required for every file processed.",
    "No sensitive user data shall be stored in plaintext.",
    "Access to the repository is restricted to authorized project members only.",
    "Any modification to the core parsing logic requires a secondary code review.",
    "Processing time for a single-page document must not exceed 2 seconds.",
    "The system must handle concurrent read operations without memory leaks.",
    "Error logs must be generated in real-time for any failed parsing attempts.",
    "All code updates must be accompanied by relevant comments.",
    "Version control commits must follow the standard naming convention: [Action] - [Description]."
]


def extract_text(file_path):
    text = ""

    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text() or ""

    return text


def check_compliance(file_path):

    try:
        document_text = extract_text(file_path)

        # Normalize text
        document_text = re.sub(r'\s+', ' ', document_text).lower()

        passed = 0
        failed = 0
        results = {}

        print("\n===== COMPLIANCE REPORT =====\n")

        for number, requirement in enumerate(requirements, start=1):

            if requirement.lower() in document_text:
                print(f"{number}. PASS: {requirement}")
                passed += 1
                results[f"Requirement {number}"] = "PASS"
            else:
                print(f"{number}. FAIL: {requirement}")
                failed += 1
                results[f"Requirement {number}"] = "FAIL"

        print("\n===== SUMMARY =====")
        print("Total Requirements:", len(requirements))
        print("Passed:", passed)
        print("Failed:", failed)

        # Generate JSON report
        generate_report(results)

    except Exception as e:
        print("Error:", e)


file_path = input("Enter PDF file name: ")
check_compliance(file_path)
