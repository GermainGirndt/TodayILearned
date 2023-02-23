from pypdf import PdfMerger

cover_letter_pdf = "2023-02-18 - Cover Letter - Pearson - Germain Girndt - Internship - English - Professional Presentations.pdf"
cv_pdf = "2023-02-17 EN - English - Software Engineer Resume-3.pdf"

pdfs = [cover_letter_pdf, cv_pdf]

merger = PdfMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("Girndt-Germain-PIB-EN3-Application-Wintersemester 2022-23.pdf")
merger.close()