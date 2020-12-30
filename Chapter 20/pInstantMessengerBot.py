#! python3

# pInstantMessengerBot.py - sends a message into a specific Discord channel

import pyautogui

discordIcon = r"Chapter 20\i_discord.PNG"
channelIcon = r"Chapter 20\i_channel.PNG"
subChannelIcon = r"Chapter 20\i_subchannel.PNG"
textBoxScreen = r"Chapter 20\i_textBox.PNG"

print('Initiating...')
pyautogui.countdown(10)

if not pyautogui.getActiveWindowTitle().endswith("Discord"):
    pyautogui.click(discordIcon)

window = pyautogui.getActiveWindow()
pyautogui.sleep(1)
window.maximize()
pyautogui.sleep(1)
pyautogui.click(channelIcon)
pyautogui.sleep(1)
pyautogui.click(subChannelIcon)
pyautogui.sleep(1)
pyautogui.click(textBoxScreen)

pyautogui.write("Instant messenger bot greets this server o7")
pyautogui.sleep(1)
pyautogui.write(['enter'])

print("Message sent.")