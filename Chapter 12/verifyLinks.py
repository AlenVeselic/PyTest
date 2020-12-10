import requests, bs4

someUrl = ""

noneExistentUrls = []
response = requests.get(someUrl)
if response.status_code == 404:
    print("Oh, so you gave me a broken link outright, eh? How could you?!")
else:

    resSoup = bs4.BeautifulSoup(response.text, 'html.parser')

    links = resSoup.select('a')

    for link in range(len(links)):
        linkCheck = requests.get(links[link].get('href'))
        if linkCheck.status_code == 404:
            noneExistentUrls.append(linkCheck.url)
            print("Broken link found!")

