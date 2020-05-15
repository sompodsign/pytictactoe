import os
import sys
import PyPDF2

password = sys.argv[1]
encryptFailed = []

for folders, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            path = os.path.join(folders, filename)
            pdfReader = PyPDF2.PdfFileReader(open(filename, 'rb'))
            if pdfReader.isEncrypted is False:
                pdfWriter = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfReader.numPages):
                    pdfWriter.addPage(pdfReader.getPage(pageNum))
                pdfWriter.encrypt(password)
                encryptedPath = path[:-4] + '_encrypted.pdf'
                encryptedVersion = open(encryptedPath, 'wb')
                pdfWriter.write(encryptedVersion)
                encryptedVersion.close()

                # Check if file was encrypted properly
                pdfReader = PyPDF2.PdfFileReader(open(encryptedPath, 'rb'))
                if (pdfReader.isEncrypted is True and pdfReader.decrypt(password) == 1):
                    os.remove(path)
                else:
                    encryptFailed.append(filename)

if encryptFailed != []:
    print('The following files failed encryption and were not deleted:')
    for filename in encryptFailed:
        print(filename)
else:
    print("All PDF's files in the folder tree have been encrypted successfully."
          "The original files have been deleted.")
