#! python3

# pCookieClickerBot.py - Plays cookie clicker to a certain degree(with graphics disabled)

import pyautogui

cookieLoc = r"Chapter 20\CookieClickerScreens\TheCookie.PNG"
pointerUpLoc = r"Chapter 20\CookieClickerScreens\New_clicker_Upgrade.PNG"
upgrade1Loc = r"Chapter 20\CookieClickerScreens\cursor_Upgrade.PNG"
upgrade2Loc = r"Chapter 20\CookieClickerScreens\granny_Upgrade.PNG"
upgrade3Loc = r"Chapter 20\CookieClickerScreens\farm_Upgrade.PNG"

print("Initializing...")
pyautogui.countdown(10)


#if not pyautogui.getActiveWindowTitle().endswith(r'Cookie Clicker – Google Chrome'):
#    print("Can't game without seeing, bruh.")


#if pyautogui.getActiveWindowTitle().endswith(r'Cookie Clicker - Google Chrome'):
cookieCoords = pyautogui.locateOnScreen(cookieLoc)
try:
    while True:
        pointerUp = pyautogui.locateOnScreen(pointerUpLoc)
        if pointerUp != None:
            pyautogui.click(pointerUp, duration = 0.5)

        farm = pyautogui.locateOnScreen(upgrade3Loc)
        while farm != None:
            pyautogui.click(farm, duration = 0.5)
            pyautogui.move(-100, 0, duration = 0.25)
            farm = pyautogui.locateOnScreen(upgrade3Loc)

            
        
        granny = pyautogui.locateOnScreen(upgrade2Loc)
        while granny != None:
            pyautogui.click(granny, duration = 0.5)
            pyautogui.move(-100, 0, duration = 0.25)
            granny = pyautogui.locateOnScreen(upgrade2Loc)

        cursor = pyautogui.locateOnScreen(upgrade1Loc)
        while cursor != None:
            pyautogui.click(cursor, duration = 0.5)
            pyautogui.move(-100, 0, duration = 0.25)
            cursor = pyautogui.locateOnScreen(upgrade1Loc)

        

        pyautogui.moveTo(cookieCoords, duration = 0.5)
        for i in range(50):
            pyautogui.click(duration = 0.1)

        pyautogui.sleep(3)

except KeyboardInterrupt:
    print("Goodbye.")