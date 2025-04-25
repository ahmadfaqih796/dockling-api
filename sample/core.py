from fastapi import FastAPI, File, UploadFile, Body
from docling.document_converter import DocumentConverter
from pydantic import BaseModel
import tempfile
import fitz
import os
import requests

app = FastAPI()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

class URLRequest(BaseModel):
    url: str

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    doc = fitz.open(file_path)
    teks = ""
    for page in doc:
        teks += page.get_text()
    doc.close()
    return {"filename": file.filename, "text": teks.replace("\n", " ")}


@app.post("/upload-file-by-url")
async def upload_file_by_url(payload: URLRequest):
    url = payload.url
    filename = url.split("/")[-1]
    file_path = os.path.join(UPLOAD_DIR, filename)

    response = requests.get(url)
    print("msasassa", response)
    with open(file_path, "wb") as f:
        f.write(response.content)

    doc = fitz.open(file_path)
    teks = ""
    for page in doc:
        teks += page.get_text()
    doc.close()

    return {"filename": filename, "text": teks}


@app.post("/upload-file-by-url2")
async def upload_file_by_url2(url : str = Body(...)):
    print("url", url)
    converter = DocumentConverter()
    result = converter.convert(url)
    markdown = result.document.export_to_markdown()
    print("vvvvvvvvvvv", result)
    
    return {
        "filename": url.split("/")[-1],
        "markdown": markdown
    }


@app.post("/upload-file-docling")
async def upload_file_docling(file: UploadFile = File(...)):
    contents = await file.read()

    # Simpan ke temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(contents)
        tmp_path = tmp.name

    # Proses dengan docling
    try:
        converter = DocumentConverter()
        result = converter.convert(tmp_path)
        markdown = result.document.export_to_markdown()
        return {
            "filename": file.filename,
            "markdown": markdown
        }
    except Exception as e:
        return {"error": str(e)}
