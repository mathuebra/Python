import pyautogui
from pynput import keyboard
import time
import math


button_pressed = (255, 204, 204)

# Tuplas de 4 posições contendo x, y, width, height de cada botão desativado

coord_colors = []
coord_colors.append(pyautogui.locateOnScreen('red_button_idle.png', confidence=0.8))
coord_colors.append(pyautogui.locateOnScreen('blue_button_idle.png', confidence=0.8))
coord_colors.append(pyautogui.locateOnScreen('green_button_idle.png', confidence=0.8))
coord_colors.append(pyautogui.locateOnScreen('yellow_button_idle.png', confidence=0.8))

def check_pressed():
    
    colors_sequence = []
    for coord in coord_colors:
        if pyautogui.pixelMatchesColor(pyautogui.center(coord), (255, 255, 255), tolerance=50):
            colors_sequence.append(pyautogui.center(coord))
            
    