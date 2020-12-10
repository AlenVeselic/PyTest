from selenium import webdriver
browser = webdriver.Firefox(executable_path=r"C:\Users\alene\Downloads\geckodriver-v0.28.0-win64\geckodriver.exe")
browser.get('https://inventwithpython.com')
linkElem = browser.find_element_by_link_text('Read Online for Free')
type(linkElem)
linkElem.click()
