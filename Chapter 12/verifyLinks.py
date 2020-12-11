import requests, bs4, re, logging

logging.basicConfig(level= logging.DEBUG, format= ' %(asctime)s - %(levelname)s - %(message)s')

someUrl = "https://slo-tech.com/forum/t2467#crta"

linkRegex = re.compile(r'^(http|https)://\w+')


nonExistentUrls = []
response = requests.get(someUrl)
if response.status_code == 404:
    print("Oh, so you gave me a broken link outright, eh? How could you?!")
else:

    resSoup = bs4.BeautifulSoup(response.text, 'html.parser')

    links = resSoup.select('#content a')
    print('There are %s links on this page.' % len(links))
    for link in range(len(links)):
        if linkRegex.search(links[link].get('href')):
            logging.debug("Regex true, url: " + str(links[link].get('href')))
            linkCheck = requests.get(links[link].get('href'))
        else:
            logging.debug("Regex false, url: " + str(links[link].get('href')))
            linkCheck = requests.get("https://slo-tech.com" + links[link].get('href'))
            
        if linkCheck.status_code == 404:
            nonExistentUrls.append(linkCheck.url)
            print("Broken link found!")

print('Done.')
print('Broken links: ' + str(nonExistentUrls))