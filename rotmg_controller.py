import time as t
import pydirectinput as pdi
import pyautogui as pauto

#Note: Must be started as administrator!
def activate_auto_nexus():
    """autoNexus based on detecting whether the pixels to the left of "HP" are Red"""

    first = True
    start_time = 0

    while True:
        if pauto.pixelMatchesColor(1574,473,[198,50,54]):
            if t.time() > start_time + 10 or first: # 10 second cooldown in between nexus key press.
                pdi.press("f")
                print("Health low, nexusing...")
                start_time = t.time()
                first = False

activate_auto_nexus()
