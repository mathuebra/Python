import pyautogui
import keyboard
import math
import time

# Centro do círculo:
# X - 2905
# Y - 590
# RGB - (244, 244, 244)

center_x = 2905
center_y = 590

radius = 100

numpoints  = 300
points = []

time.sleep(1) #tempo para mudar para a página

def check_quit():
    if keyboard.is_pressed('q'):
        return True
    return False

for i in range(numpoints):
    angle = i * (2*math.pi) / numpoints
    x = int(center_x + radius * math.cos(angle))
    y = int(center_y + radius * math.cos(angle))
    points.append((x,y))


pyautogui.moveTo(points[0][0], points[0][1])
pyautogui.mouseDown()

for point in points[1:]:
    pyautogui.moveTo(point[0], point[1])
    time.sleep(0.01)
    if check_quit():
        break

pyautogui.mouseUp()


