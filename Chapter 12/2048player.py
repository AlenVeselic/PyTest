# Play the game 2048 using Selenium

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import pyinputplus as pyip 

import time, logging

logging.basicConfig(level = logging.DEBUG, format = ' %(asctime)s - %(levelname)s - %(message)s')

tries = pyip.inputInt(prompt="How many loops should the bot go through?")

driver = webdriver.Firefox(executable_path=r"C:\Users\alene\Downloads\geckodriver-v0.28.0-win64\geckodriver.exe")

driver.get('https://play2048.co/')

window = driver.find_element_by_css_selector('html')

scores = []

for i in range(tries):
    logging.debug('Iteration number ' + str(i + 1))
    if len(driver.find_elements_by_class_name("game-over")) == 0: 
        


        time.sleep(1)

        window.send_keys(Keys.UP)

        time.sleep(1)

        window.send_keys(Keys.DOWN)

        time.sleep(1)

        window.send_keys(Keys.LEFT)

        time.sleep(1)

        window.send_keys(Keys.RIGHT)
    else:
        curScore = driver.find_element_by_class_name('score-container')
        scores.append(curScore.text)
        retry = driver.find_element_by_class_name('retry-button')
        retry.click()

curScore = driver.find_element_by_class_name('score-container')
scores.append(curScore.text)

print('Games played: ' + str(len(scores)))

for score in range(len(scores)):
    print(str(score + 1) + '. game score: ' + str(scores[score]))
print("Program's finished")   