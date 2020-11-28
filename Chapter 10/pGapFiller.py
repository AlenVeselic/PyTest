from pathlib import Path
import re, os, shutil

regexNum = re.compile(r'(^[A-Za-z]*)(\d+)(\.\w{3})')


somePath = Path(r'C:\Users\alene\gapFillTestFolder')
matchVar = 0
prefixes = []
matches = []

print(os.listdir(somePath))


for fileName in os.listdir(somePath):
    mo = regexNum.search(fileName)
    if mo != None:
        print('Match: ' + mo.group())
        print('Match in pieces:' + mo.group(1)+ " " + mo.group(2)+ " " + mo.group(3))
        if mo.group(1) not in prefixes:
            prefixes.append(mo.group(1))
        matches.append(mo)



print('match prefixes:')
for item in prefixes:
    print(item)

for prefix in prefixes:
    num = 1000
    for match in matches:
        
        if prefix in match.group(0) and int(match.group(2)) < num:
            num = int(match.group(2))
        if prefix in match.group(0) and int(match.group(2)) > num + 1:
            #shutil.move(somePath / match.group(0))# rename file
            # for each number between next group(2)
            # newFile = open(match.group(1) + (num + 1) + match.group(3), 'w') 
            # newFile.close()

            # print(f'Renaming {match.group(0)} to {match.group(1)}{num + 1}{match.group(3)}')
            num = num + 1
        if prefix in match.group(0) and int(match.group(2)) == num + 1:
            num = num + 1
    
    


    
