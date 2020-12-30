import pyautogui, time
time.sleep(5)
pyautogui.click()
distance = 200
change = 5
while distance > 0:
    pyautogui.drag(distance, 0, 0.5, button='left')     # Move right.
    distance = distance - change
    pyautogui.drag(0, distance, 0.5, button='left')     # Move down.
    pyautogui.drag(-distance, 0, 0.5, button='left')    # Move left.
    distance = distance - change
    pyautogui.drag(0, -distance, 0.5, button='left')    # Move up.