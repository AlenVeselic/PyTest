from pathlib import Path
import os, shutil

folderPath = Path.home()

srcPath = Path(r'C:\Users\alene\Downloads')

for foldername, subfolder, filenames in os.walk(srcPath):

    for filename in filenames:
        if filename.endswith('.pdf') or filename.endswith('.jpg'):
            shutil.copy(folderPath / foldername / filename, folderPath / 'test2' )