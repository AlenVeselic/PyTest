import PyPDF2

word = open(r"C:\Users\alene\Downloads\automate_online-materials\dictionary.txt")

words = word.readlines()
word.close()

for i in words:
    print("Checking word: " + i[:-1])
    filePdf = open(r"C:\Users\alene\Desktop\Random PDFs\watermarkedCover_encrypted.pdf" ,'rb')
    readPDF = PyPDF2.PdfFileReader(filePdf)
    if readPDF.decrypt(i[:-1].upper()) == 1:
        password = i[:-1].upper()
        break
    if readPDF.decrypt(i[:-1].lower()) == 1:
        password = i[:-1].lower()
        break
if password != None:
    print("The password is: " + password)
else:
    print("No password found.")
print('Done.')
