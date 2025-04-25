from docling.document_converter import DocumentConverter

source = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy"
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown()) 