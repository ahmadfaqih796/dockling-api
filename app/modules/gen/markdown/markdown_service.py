import os
import fitz
import requests
import tempfile
from docling.document_converter import DocumentConverter

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def save_upload_file(file, filename="dummy.pdf"):
    file_path = os.path.join(UPLOAD_DIR, filename)
    with open(file_path, "wb") as f:
        f.write(file)
    return file_path

def extract_text_from_pdf(file_path: str):
    doc = fitz.open(file_path)
    teks = "".join([page.get_text() for page in doc])
    doc.close()
    return teks.strip()

def download_file_from_url(url: str):
    filename = url.split("/")[-1]
    file_path = os.path.join(UPLOAD_DIR, filename)
    response = requests.get(url)
    with open(file_path, "wb") as f:
        f.write(response.content)
    return file_path, filename

def convert_to_markdown_from_url(url: str):
    converter = DocumentConverter()
    result = converter.convert(url)
    return result.document.export_to_markdown()

def convert_to_markdown_from_file(contents, filename: str):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(contents)
        tmp_path = tmp.name
    converter = DocumentConverter()
    result = converter.convert(tmp_path)
    return result.document.export_to_markdown()
