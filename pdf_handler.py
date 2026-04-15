from PyPDF2 import PdfReader

def extract_text_from_pdfs(pdf_files):
    documents = []

    for pdf in pdf_files:
        reader = PdfReader(pdf)

        for i, page in enumerate(reader.pages):
            text = page.extract_text()

            if text:
                documents.append({
                    "content": text,
                    "page": i + 1   # page number
                })

    return documents