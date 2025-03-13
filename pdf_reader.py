import PyPDF2
import sys

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            num_pages = len(reader.pages)
            
            print(f"PDF has {num_pages} pages.")
            print("=" * 50)
            
            for page_num in range(num_pages):
                page = reader.pages[page_num]
                text = page.extract_text()
                
                print(f"\n--- Page {page_num + 1} ---\n")
                print(text)
                print("=" * 50)
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python pdf_reader.py <path_to_pdf>")
    else:
        pdf_path = sys.argv[1]
        extract_text_from_pdf(pdf_path) 