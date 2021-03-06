
# PRACTICE PROJECT: Image Site Downloader (Imgur)

# TODO: OPEN IMGUR
#       USE QUERY IN SEARCH BAR
#       DOWNLOAD IMAGES GENERATED FROM SEARCH
#

import bs4, requests, webbrowser, os, time, logging
from pathlib import Path
logging.basicConfig(level = logging.DEBUG, format =' %(asctime)s - %(levelname)s - %(message)s')

print('What would you like to search for? ')

query = input()

querySite = requests.get("https://imgur.com/search?q=" + query)
querySite.raise_for_status()

querySoup = bs4.BeautifulSoup(querySite.text, 'html.parser')

imageLocs = querySoup.select('.post a')

thumbSoup = querySoup.select('.post a img')

os.makedirs(query, exist_ok=True)

# imgur generates it's post sites using js so I couldn't get high fidelity pics by crawling into every post generated by the query, therefore I decided
# to just download the post thumbnails, since the site generated by a query shows 60 posts before adding more with the help of pagination

# I would otherwise have loved to tackle it the way I thought, but there's undoubtedly a better way and am only settling on this because I don't believe
# that the scope of this practice project demands post images, but just the ones generated by the query

for post in range(len(imageLocs)):
    time.sleep(5)
    print('Post number ' + str(post + 1) + "'s thumb link is: " + imageLocs[post].get('href'))

    # logging.debug('Post text: ' + str(postSoup))

    if thumbSoup == []:
        print('No thumbnails found.')
    else:

        
       currentImageUrl = 'https:' + thumbSoup[post].get('src')

       currentImage = requests.get(currentImageUrl)
       currentImage.raise_for_status()

       imageFile = open(Path.cwd() / query / os.path.basename(currentImageUrl), 'wb')
       

       for chunk in currentImage.iter_content(100000):
           imageFile.write(chunk)
        
       imageFile.close() 






