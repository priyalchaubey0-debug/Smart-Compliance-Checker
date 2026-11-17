Smart Compliance Checker
A Python-based application that extracts text from PDF documents and checks whether predefined compliance requirements are present in the document.

The application automates basic document verification by scanning PDF content, evaluating 11 predefined compliance requirements, and displaying the results in a clear PASS/FAIL format.
Features
- Extracts text from PDF documents.
- Reads PDF content page by page.
- Checks 11 predefined compliance requirements.
- Displays individual PASS/FAIL results.
- Provides a summary of compliance checks.
- Saves extracted PDF text into a separate text file.
- Handles basic PDF reading and extraction errors.
Technologies Used
- Python – Core programming language.
- PyPDF2 – PDF text extraction.
- File Handling – Reading PDF files and saving extracted te
- Project Structure
- Smart-Compliance-Checker/
├── reader.py
├── compliance_checker.py
├── sample.pdf
├── extracted_text.txt
├── .gitattributes
└── README.md
Installation
1. Clone the repository:
git clone https://github.com/priyalchaubey0-debug/Smart-Compliance-Checker.git
2. Navigate to the project directory:
cd Smart-Compliance-Checker
3. Install the required dependency:
pip install PyPDF2
Usage
1. Place the PDF document you want to analyze in the project directory.
2. Run the application:
python compliance_checker.py
3. The application will:
   - Extract text from the PDF.
   - Evaluate the predefined compliance requirements.
   - Display PASS/FAIL results for each requirement.
   - Generate a summary of the checks.
   - Save the extracted text in extracted_text.txt.
Output
The application displays the results of all 11 compliance checks in the terminal.
- PASS: The required text or condition was found.
- FAIL: The required text or condition was not found.
The extracted PDF content is also saved in extracted_text.txt for reference.
Limitations
- The application uses predefined text-matching rules.
- It does not perform advanced semantic analysis.
- A PASS result only indicates that the expected text was found; it does not guarantee actual legal or regulatory compliance.
- Results depend on the quality and extractability of PDF text.
Future Improvements
- Support for multiple PDF documents.
- Customizable compliance requirements.
- Improved text matching and semantic analysis.
- Detailed compliance reports.
- Support for additional document formats.
Author
Priyal Chaubey
