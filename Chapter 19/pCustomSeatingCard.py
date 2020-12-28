#! python3

# pCustomSeatingCard.py - generate custom seating card images for your guests

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import os

guestsPath = r"C:\Users\alene\Downloads\automate_online-materials\guests.txt"
stockFlowers = r"C:\Users\alene\Desktop\Projects\Web Development\Projects\PyTest\Chapter 19\toppng.com-tropical-flower-cartoon-transparent-this-backgrounds-watercolor-flowers-clipart-998x488.png"
floIm = Image.open(stockFlowers)
floIm = floIm.resize((200, 100))
fontsFold = r"C:\Windows\Fonts"
fontObj = ImageFont.truetype(os.path.join(fontsFold, 'LatoWeb-Light.ttf'), 25)
os.makedirs('seatingCards', exist_ok= True)

guestFile = open(guestsPath)
guests = guestFile.readlines()

for guest in range(len(guests)):
    card = Image.new('RGBA', (288, 360), 'antiquewhite')

    cardDraw = ImageDraw.Draw(card)

    cardDraw.rectangle((10, 10, 278, 350), outline = 'black')

    cardDraw.text((75, 100), guests[guest], fill = 'orange', font = fontObj)

    card.paste(floIm, (card.width - floIm.width - 10, card.height - floIm.height - 10), floIm)
    print('Creating seating card for %s...' % guests[guest])
    fileName = guests[guest][:-1] + str(guest) + '.png'
    card.save(os.path.join("./seatingCards", fileName ))
print('Cards finished. You can find them in the "seatingCards" folder')





    

