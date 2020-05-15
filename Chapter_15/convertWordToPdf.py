import win32com.client # install with "pip install pywin32==224"
import docx
wordFilename = 'CV-Sumaiya-Nasrin.docx'
pdfFilename = 'convertedfromword.pdf'

# doc = docx.Document()
# # Code to create Word document goes here.
# doc.save(wordFilename)

wdFormatPDF = 17 # Word's numeric code for PDFs.
wordObj = win32com.client.Dispatch('Word.Application')

docObj = wordObj.Documents.Open(wordFilename)
docObj.SaveAs(pdfFilename, FileFormat=wdFormatPDF)
docObj.Close()
wordObj.Quit()
