
from flask import Flask, render_template, request
from compliance_checker import requirements, extract_text
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    results = None

    if request.method == "POST":
        pdf = request.files["pdf"]

        if pdf and pdf.filename.endswith(".pdf"):
            text = ""

            from PyPDF2 import PdfReader
            reader = PdfReader(pdf)

            for page in reader.pages:
                text += page.extract_text() or ""

            text = re.sub(r'\s+', ' ', text).lower()

            results = []
            for req in requirements:
                status = "PASS" if req.lower() in text else "FAIL"
                results.append({"requirement": req, "status": status})

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
