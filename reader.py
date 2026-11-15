
import PyPDF2
import os
from datetime import datetime

def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            print(f"Total pages: {len(reader.pages)}")

            extracted_text = ""

            for page_number, page in enumerate(reader.pages, start=1):
                text = page.extract_text() or ""
                extracted_text += text + "\n"

            print(extracted_text)

            # Save extracted text
            with open("extracted_text.txt", "w", encoding="utf-8") as output:
                output.write(extracted_text)

            print("\nText saved successfully!")

    except Exception as e:
        print(f"Error: {e}")


read_pdf("sample.pdf")
