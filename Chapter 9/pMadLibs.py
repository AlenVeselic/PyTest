from pathlib import Path 
import sys, os, re
import pyinputplus as pyip

#if sys.argv[0] == None:
#    print('Haha funny madlib containing file not given')
#else:
mlPath = Path(r'C:\Users\alene\Desktop\Projects\Web Development\Projects\PyTest\Chapter 9') / 'crazytext.txt'

emptyMadLib = open(mlPath)
content = emptyMadLib.read()
emptyMadLib.close()



userWords = []
doneLib = ''
skipSpaces = 0

kWordRegex = re.compile(r'\s(adjective|noun|adverb|verb)+(\s|\.)+', re.I)
dotRegex = re.compile(r'.\.\s$')
wordRegex = re.compile(r'[A-Za-z]+(\s|\.)*')

num = kWordRegex.findall(content)
print(len(num))
for letter in range(len(content)):


    findWord = kWordRegex.search(content[letter:])
    if findWord != None:
        print(findWord.span(), findWord.group(1),findWord.group(2))
    if findWord != None and findWord.start() == 0:

        print('Give us a ' + findWord.group(1) + ' would you?')
        userInput = pyip.inputStr()
        doneLib += ' ' + userInput
        if dotRegex.search(findWord.group()) != None:
            doneLib += '. '
        else:
            doneLib += ' '
        skipSpaces = findWord.end()
    
    if skipSpaces > 0:
        skipSpaces -= 1
        continue
        

    doneLib += content[letter]

print(doneLib)
filledLib = open('nuovoLib.txt', 'w')
filledLib.write(doneLib)
