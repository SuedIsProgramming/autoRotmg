import time as t
import pydirectinput as pdi
import pyautogui as pauto
import sys
import ctypes, os


def is_admin():
    """Returns true if the IDE is in administrator mode."""
    try:
        is_adm = os.getuid() == 1
    except AttributeError:
        is_adm = ctypes.windll.shell32.IsUserAnAdmin() == 1

    return is_adm

def activate_auto_nexus():
    """autoNexus based on detecting whether the pixels to the left of "HP" are Red"""

    if not is_admin(): # Checks if the IDE is in administrator mode. If not, exits.
        print('No admin privilages. Program will not work.')
        return

    first = True
    start_time = 0

    while True:
        if pauto.pixelMatchesColor(1574,473,[198,50,54]):
            if t.time() > start_time + 10 or first:
                pdi.press("f")
                print("Health low, nexusing...")
                start_time = t.time()
                first = False

activate_auto_nexus()
