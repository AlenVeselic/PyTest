#! python

# pGetText.py - finds a notepad window and get all the text in it
import pyautogui, pyperclip

NoteIcon = r"Chapter 20\NotepIcon.PNG"

print('Prepare for initiation!')
pyautogui.countdown(10)

if not pyautogui.getActiveWindowTitle().endswith('Beležnica'):
    pyautogui.click(NoteIcon)

window = pyautogui.getActiveWindow()

window.maximize()

pyautogui.moveTo(window.height/2, window.width/2, duration = 0.3)

pyautogui.click()
pyautogui.hotkey('ctrl','a')
pyautogui.hotkey('ctrl','c')

print('The text in your notepad is: ' + pyperclip.paste())

print("Done")