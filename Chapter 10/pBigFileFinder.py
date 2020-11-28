import os
from pathlib import Path

somePath = Path(r'H:\Games\The Punisher')

bigFiles = []

for folderName, subfolders, filenames in os.walk(somePath):
    for filename in filenames: 
        print(f'Checking {folderName} \\ {filename}...')
        print(f'Size: {os.path.getsize(Path(folderName) / filename) * (10**(-6))}MB')
        if os.path.getsize(Path(folderName) / filename) * (10**(-6)) > 100:
            # send2trash.send2trash(Path(folderName) / filename) - this would delete the big files, also you need to import send2trash for this to work
            bigFiles.append(Path(folderName) / filename)

print('All the big files are: ')
for item in bigFiles:
    print(item)