# Python code for extracting content from documents (PDF, PowerPoint)

import subprocess

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extract text from PDF using a C++ backend or Python libraries."""
    # For example, calling C++ code via subprocess
    result = subprocess.run(['./cpp_modules/file_parser'], input=pdf_path, text=True, capture_output=True)
    return result.stdout

def process_content(content: str) -> str:
    """Process and clean the extracted content."""
    # Some basic preprocessing (e.g., removing special characters)
    return content.replace("\n", " ").strip()
