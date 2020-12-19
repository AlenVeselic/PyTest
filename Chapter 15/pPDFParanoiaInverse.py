#! python3

# pPDFParanoiaInverse.py - find all encrypted pdf files in a directory and decrypt them. Output a decrypted version of each pdf.

import PyPDF2, os, logging

filePath = r"C:\Users\alene\Desktop\Random PDFs"
resultFilePath = r"C:\Users\alene\Desktop\Random PDFs\results"
passwort = "chamberlain"

for folder, subfolders, files in os.walk(filePath):
    if folder == resultFilePath:
        continue
    if files != []:
        for fileName in files:
            if fileName.endswith('.pdf'):
                print("Checking " + fileName + "...")
                filePDF = open(folder + "\\" + fileName, 'rb')
                pdfRead = PyPDF2.PdfFileReader(filePDF)
                if pdfRead.isEncrypted:
                    if pdfRead.decrypt(passwort) == 1:
                        pdfWrite = PyPDF2.PdfFileWriter()
                        for pageNum in range(pdfRead.numPages):
                            pdfWrite.addPage(pdfRead.getPage(pageNum))
                        
                        unencryptedPDF = open(resultFilePath + '\\' + fileName[:-14] + ".pdf", 'wb')

print('Done.')


