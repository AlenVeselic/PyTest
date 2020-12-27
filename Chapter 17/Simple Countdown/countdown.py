#! python3
# countdown.py - A simple countdown script.

import time, subprocess

timeLeft = 60

while timeLeft > 0:
    print(timeLeft, end='', flush=True)
    time.sleep(1)
    timeLeft = timeLeft - 1

# At the end of the countdown, play a sound file.
subprocess.Popen(['start', r'H:\Games\SteamLibrary\steamapps\common\hotline_miami\Hydrogen.ogg'], shell = True)