import os, sys, PyPDF2

password = sys.argv[1]
decryptFailed = []

for folders, subfolders, filenames in os.walk('.'):
    for filename in filenames:
        if filename.endswith('.pdf'):
            path = os.path.join(folders, filename)
            pdfReader = PyPDF2.PdfFileReader(open(path, 'rb'))
            if pdfReader.isEncrypted is True:
                if pdfReader.decrypt(password) != 1:
                    print(filename, ' failed to decrypt.')
                    decryptFailed.append(filename)
                else:
                    pdfWriter = PyPDF2.PdfFileWriter()
                    for pageNum in range(pdfReader.numPages):
                        pdfWriter.addPage(pdfReader.getPage(pageNum))

                    decryptedPath = path[:-4] + '_decrypted.pdf'
                    decryptedVersion = open(decryptedPath, 'wb')
                    pdfWriter.write(decryptedVersion)
                    decryptedVersion.close()

if decryptFailed != []
    print('files listed below are not decrypted.')
    for file in decryptedFailed:
        print(file)
else:
    print('All encrypted files are decrypted successfully and original files are kept.')
