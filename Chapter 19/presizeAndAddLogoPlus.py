#! python3

# resizeAndAddLogo.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os, logging
logging.basicConfig(level = logging.DEBUG, format = " %(asctime)s - %(levelname)s - %(message)s")
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logoIm = Image.open(LOGO_FILENAME)
logoIm = logoIm.resize((75,100))
logoWidth, logoHeight = logoIm.size

extensions = ['.jpg', '.png', '.gif', '.bmp']

os.makedirs('withLogo', exist_ok = True)
# Loop over all files in the working directory.
for filename in os.listdir('.'):
    logging.debug(filename[-4:])
    if not(filename[-4:].lower() in extensions) or filename == LOGO_FILENAME:
        continue    # skip non-image files and the logo file itself

    im = Image.open(filename)
    width, height = im.size

    # Check if image needs to be resized.
    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        # Calculate the new width and height to resize to.
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE

        # Resize the image.
        print('Resizing %s...' % (filename))
        im = im.resize((width, height))

    if width < (2 * logoWidth) or height < (2 * logoHeight):
        print("Image too small, skipping watermark addition.")
    else:
        # Add the logo.
        print('Adding logo to %s...' % (filename))
        im.paste(logoIm, (width - logoWidth, height - logoHeight), logoIm)

    # Save changes.
    im.save(os.path.join('withLogo', filename))