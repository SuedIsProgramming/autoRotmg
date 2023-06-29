import time as t
import pyautogui as pauto
import pygetwindow as gw
import pytesseract as ptsrct

t.sleep(1)
FACES_NOTEPAD = r"C:\Users\thesi\Documents\GitHub\autoRotmg\images\testingLocateWindow.bmp"
HP_TESARACT_TESTING=r"C:\Users\sueds\Documents\GitHub\autoRotmg\images\testingTesaractHealth.bmp"

#loc = pauto.locateOnWindow(FACES_NOTEPAD,grayscale=True,title=gw.getActiveWindow().title) #Unsure why its not working
#loc = pauto.locateOnScreen(FACES_NOTEPAD,grayscale=True)

print(ptsrct.image_to_string(HP_TESARACT_TESTING, lang='eng'))
#if  loc is None:
#    print('Can\'t find it')
#else:
#    print('Found it at', loc) 
          
