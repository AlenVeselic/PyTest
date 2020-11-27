from pathlib import Path
import re, os
import pyinputplus as pyip

#use glob to find txt files

p = Path(r'H:\The Folder of many text files')

p.glob('*.txt')

txtFiles = list(p.glob('*.txt'))



regExUserInput = pyip.inputRegexStr(prompt='Please provide a regex to search for: ')

print(regExUserInput)

regExUser = regExUserInput

for fileN in txtFiles:
    curFile = open(fileN)
    curFileLines = list(curFile.readlines())
    for line in range(len(curFileLines)):
        if regExUser.search(curFileLines[line]) != None:
            print('Match found in line ' + str(line) + '.\nIn file: ' + os.path.basename(fileN) +'. \nLine: ' + curFileLines[line])
            print()

