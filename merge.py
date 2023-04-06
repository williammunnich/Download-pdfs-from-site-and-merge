#This file combines pdf files given names are put in pdfs list. All pdfs should be in the same folder
from PyPDF2 import PdfMerger

pdfs = ["example1.pdf", "example2.pdf", "example3.pdf"]

merger = PdfMerger()
for pdf in pdfs:
    merger.append(pdf)
    
merger.write("merged.pdf")
merger.close()

