import fitz

doc = fitz.open("contoh.pdf")

for halaman in doc:
    print(halaman.get_text())

doc.close()