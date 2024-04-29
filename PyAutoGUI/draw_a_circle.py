import pyautogui
from pynput import keyboard
import time
import math

pyautogui.alert("""             Pressione OK para começar! 
       pressione 'q' a qualquer momento para parar!""", title="Draw a circle", button="OK")

# coordinates = 708, 435
# radius = 200

center_x = 708
center_y = 435
radius = 200
num_points = 500

points = []

def check_quit(key):
    return key == keyboard.Key.q

def on_press(key):
       if check_quit(key):
              return False

def circle_points():
       
       for i in range(num_points):
              angle = 2 * math.pi * i / num_points
              x = center_x + radius * math.cos(angle)
              y = center_y + radius * math.sin(angle)
              points.append((round(x), round(y)))
              
       return points

points = circle_points()

pyautogui.moveTo(points[0])
pyautogui.mouseDown(button='left')

#nao ta clicando

with keyboard.Listener(on_press=on_press) as listener:
    for point in points:
       pyautogui.moveTo(point, _pause=False)
       if listener.running is False:
              break
     
pyautogui.mouseUp(button='left')