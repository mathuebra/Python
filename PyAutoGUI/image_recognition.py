import pyautogui
import keyboard
import time

yt_x = 3316
yt_y = 700

time.sleep(2)

if pyautogui.locateOnScreen('youtube.png', grayscale = True, confidence = 0.7):
    pyautogui.moveTo(yt_x, yt_y)
    pyautogui.mouseDown()
    time.sleep(0.05)
    pyautogui.mouseUp()

