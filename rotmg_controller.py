import time as t
import keyboard
import pyautogui as pauto



#pauto.displayMousePosition()
t.sleep(2)
FIRST = True
start_time = 0
print("working...")

while True:
    print("working...")
    if pauto.pixelMatchesColor(1616,472,[120,194,55]):
        continue
    elif t.time() > start_time + 10 or FIRST:
        pauto.press("f")
        start_time = t.time()
        FIRST = False
    if keyboard.is_pressed('f10'):
        break