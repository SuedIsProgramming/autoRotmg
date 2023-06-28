import time as t
import pyautogui as pauto
import pygetwindow as gw
import cv2

t.sleep(1)
FACES_NOTEPAD = r"C:\Users\thesi\Documents\GitHub\autoRotmg\images\testingLocateWindow.bmp"

loc = pauto.locateOnWindow(FACES_NOTEPAD,grayscale=True,title=gw.getActiveWindow().title) #Unsure why its not working
#loc = pauto.locateOnScreen(FACES_NOTEPAD,grayscale=True)

if  loc is None:
    print('Can\'t find it')
else:
    print('Found it at', loc) 
          
