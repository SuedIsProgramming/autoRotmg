from datetime import datetime as dt
import time as t
import ctypes, os
import pydirectinput as pdi
from PIL import ImageGrab

def is_admin():
    """Returns true if the IDE is in administrator mode."""
    try:
        is_adm = os.getuid() == 1
    except AttributeError:
        is_adm = ctypes.windll.shell32.IsUserAnAdmin() == 1

    return is_adm

def run_autonexus():
    """autoNexus based on detecting whether the pixels to the left of "HP" are Red"""

    if not is_admin(): # Checks if the IDE is in administrator mode. If not, exits.
        print('No admin privilages. Program will not work.')
        return

    first = True
    start_time = 0

    while True:
        if  (198,50,54) == ImageGrab.grab().getpixel((1574, 473)): # New implementation without the 10k limit
            if t.time() > start_time + 10 or first:
                pdi.press("f")
                print("Health low, attempted to nexus at ", dt.now())
                start_time = t.time()
                first = False

run_autonexus()
