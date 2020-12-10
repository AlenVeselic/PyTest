#! python3

# cmdEmail - sends an email from the users gmail account

#       Inputs:     Recipient email, message and when selenium reaches gmail login it prompts the user to put it in into the command line

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import pyinputplus as pyip 

import sys, time


receiver = pyip.inputEmail(prompt="Please put in mail of recipient: ")

message = pyip.inputStr(prompt="What would you like to send?")

driver = webdriver.Firefox(executable_path=r"C:\Users\alene\Downloads\geckodriver-v0.28.0-win64\geckodriver.exe")

driver.get('https://medium.com/')

btnSign = driver.find_element_by_link_text('Sign In')

btnSign.click()

btnSign = driver.find_element_by_link_text('Sign in with Google')

btnSign.click()

mailElem = driver.find_element_by_id('identifierId')

mailElem.send_keys('Your mail')

time.sleep(1)

mailElem.send_keys(Keys.ENTER)

pwd = pyip.inputPassword(prompt="Email password: ")

pwdElem = driver.find_element_by_name('password')

pwdElem.clear()

pwdElem.send_keys(pwd)

pwdElem.send_keys(Keys.ENTER)
time.sleep(1)
driver.get('https://mail.google.com/')

time.sleep(1)

composeElem = driver.find_element_by_class_name('T-I-KE')

composeElem.click()

time.sleep(10)

recipientElem = driver.find_element_by_name('to')

recipientElem.send_keys(receiver)

subjectElem = driver.find_element_by_name('subjectbox')

subjectElem.send_keys('BOT TEST')

messageElem = driver.find_element_by_class_name('editable')

messageElem.send_keys(message)

sendElem = driver.find_element_by_css_selector('[data-tooltip="Send ‪(Ctrl-Enter)‬"]')

sendElem.click()

