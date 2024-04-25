import pyautogui
import time

time.sleep(3)

youtube_button = pyautogui.center(pyautogui.locateOnScreen('image.png', grayscale=True, confidence= 0.8))

pyautogui.moveTo(youtube_button, duration=pyautogui.MINIMUM_DURATION)
pyautogui.mouseDown(button='left')
time.sleep(0.05)
pyautogui.mouseUp(button='left')
