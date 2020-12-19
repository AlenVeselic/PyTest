#! python3

# pPDFParanoia.py - encrypts all pdf files in a directory

import os, PyPDF2, logging, send2trash

logging.basicConfig(level= logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')

filePath = r"C:\Users\alene\Desktop\Random PDFs"
passwort = 'chamberlain'
for folder, subfolders, files in os.walk(filePath):
    logging.debug("Current folder: " + folder)
    
    if subfolders != []:
        logging.debug("This folder's subfolders are: ")
        for folderName in subfolders:
            logging.debug(folderName)
    if files != []:
        logging.debug("This folder's files: ")
        for fileName in files:
            logging.debug(fileName)
            if fileName.endswith('_encrypted.pdf'):
                encryptedPdf = open(folder + "\\" + fileName, 'rb')
                if PyPDF2.PdfFileReader(encryptedPdf).isEncrypted:
                   if PyPDF2.PdfFileReader(encryptedPdf).decrypt(passwort) == 1:
                       print("Deleting original unencrypted file: " + fileName[:-14] + ".pdf")
                        # send2trash.send2trash(folder + "\\" + fileName[:-14] + ".pdf")
                continue
            if fileName.endswith('.pdf'):
                print("ENCRYPTING: " + fileName)
                pdfFile = open(folder + '\\' + fileName, 'rb')
                pdfRead  = PyPDF2.PdfFileReader(pdfFile)
                pdfWrite = PyPDF2.PdfFileWriter()
                for pageNum in range(pdfRead.numPages):
                    pdfWrite.addPage(pdfRead.getPage(pageNum))
                pdfWrite.encrypt(passwort)
                resultPDF =  open(folder + "\\" + fileName[:-4] + '_encrypted.pdf', 'wb')
                pdfWrite.write(resultPDF)
                resultPDF.close()
                pdfFile.close()
                print(fileName + " ENCRYPTED.")
            
# for folder, subfolders, files in os.walk(filePath):
#    if files != []:
#        print('Checking for proper decryption...')
#        for fileName in files:
#            if fileName.endswith('_encrypted.pdf'):
#                encryptedPdf = open(folder + "\\" + fileName, 'rb')
#                if PyPDF2.PdfFileReader(encryptedPdf).isEncrypted:
#                    if PyPDF2.PdfFileReader(encryptedPdf).decrypt(passwort) == 1:
#                        print("File is properly encrypted. \n Deleting original unencrypted file: " + fileName[:-14] + ".pdf")
                        # send2trash.send2trash(folder + "\\" + fileName[:-14] + ".pdf")
#                encryptedPdf.close()
                

    print("\n")
print('Done.')