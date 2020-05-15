import PyPDF2, os

pdf_files = []
for filename in os.listdir("."):
    if filename.endswith('.pdf'):
        pdf_files.append(filename)
pdf_files.sort(key=str.lower)

pdf_writer = PyPDF2.PdfFileWriter()

for filename in pdf_files:
    pdfFileObj = open(filename, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdfFileObj)

    for pageNum in range(1, pdf_reader.numPages):
        pageObj = pdf_reader.getPage(pageNum)
        pdf_writer.addPage(pageObj)

pdfOutput = open('allminutes.pdf', 'wb')
pdf_writer.write(pdfOutput)
pdfOutput.close()