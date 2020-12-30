#! python3

# pnudge.py - nudges the mouse slightly when an interval of time passes

import pyautogui

try:

    while True:

        pyautogui.countdown(30)
        pyautogui.move(25, 25, duration = 0.3)


except KeyboardInterrupt:
    print("Done.")