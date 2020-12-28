#! python3

# pFindPhotoFolders.py - looks for photo folders in a certain directory(meant to be on a drive) and prints 
#   their absolute paths into the cmd line
#           What falls into the photo folder category?
#               - more than half the files need to be photos
#               - a photo is an image whose width and height are both greater than 500px

import os, logging, pprint

logging.basicConfig(level = logging.DEBUG, format = " %(asctime)s - %(levelname)s - %(message)s")

from PIL import Image
from pathlib import Path

testPath = Path(r"H:\Games")
extensions = ['.jpg', '.png', '.gif', '.bmp']
photoFolders = []

for foldername, subfolders, filenames in os.walk(testPath):
    
    numPhotos = 0
    fileNum = len(filenames)
    logging.debug("The number of files in folder %s is %s" % (foldername, str(len(filenames))))
    for filename in filenames:
        
        # Check if file extension isn't .png or .jpg.
        if not(filename[-4:] in extensions):
            continue # skip to next filename
        
        # Open image file using Pillow.
        try:
            im = Image.open(Path(foldername) / filename)
            width, height = im.size
        except Image.UnidentifiedImageError:
            continue

        # Check if width & height are larger than 500.
        if width > 500 and height > 500:
            # Image is large enough to be considered a photo.
            numPhotos += 1
        else:
            # Image is too small to be a photo
            continue
        # If more than half of files were photos,
        # print the absolute path of the folder.
    if numPhotos > (fileNum / 2):
        photoFolders.append(foldername)

print("Done.")
pprint.pprint(photoFolders)