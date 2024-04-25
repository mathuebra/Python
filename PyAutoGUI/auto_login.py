import sys
import pyautogui
import time

# python3 nome_do_arquivo.py 'navegador'

pyautogui.press('win')
time.sleep(0.5)
pyautogui.write('opera')
time.sleep(0.5)

browser_button = pyautogui.center(pyautogui.locateOnScreen('opera.png', grayscale=True, confidence=0.8))

pyautogui.doubleClick(browser_button, interval=0.15)

time.sleep(2)
