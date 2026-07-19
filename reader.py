import PyPDF2

def read_pdf(file_path):
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            print(f"Total pages: {len(reader.pages)}")
            
            
            page = reader.pages[0]
            print(page.extract_text())
            
    except Exception as e:
        print(f"Error: {e}")

read_pdf('sample.pdf')
