# PyPDF

## Merge and Split PDFs

```
pip install pdf
```

### Code

- Some features

```
from pypdf import PdfReader

reader = PdfReader("example.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()
```

- Merging

```
from pypdf import PdfMerger

pdfs = ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf']

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
```

### Docu

```
https://pypdf.readthedocs.io/en/stable/index.html
```
