import pyautogui
from pynput import keyboard
import time
import sys

pyautogui.alert("""             Pressione OK para começar! 
       pressione 'q' a qualquer momento para parar!""", title="Google Dinossaur", button="OK")

cactus_pixel = (550, 545)
retry_pixel = (712, 513)
cactus_rgb = (83, 83, 83)
background_rgb = (247, 247, 247)

stop_program = False

def on_press(key):
    global stop_program
    if key == keyboard.Key.q:
        stop_program = True
        return False

def check_endgame():
    if pyautogui.pixelMatchesColor(retry_pixel[0], retry_pixel[1], cactus_rgb):
        return True
    return False
        
def check_cactus():
    if pyautogui.pixelMatchesColor(cactus_pixel[0], cactus_pixel[1], cactus_rgb):
        pyautogui.press('up', _pause=False)

with keyboard.Listener(on_press=on_press) as listener:
    while not stop_program:
        if check_endgame():
            pyautogui.click(button='left', x=retry_pixel[0], y=retry_pixel[1])
            pyautogui.moveTo(cactus_pixel)
        check_cactus()

# Encerra o programa completamente após a interrupção
sys.exit()
