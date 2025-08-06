# pip install PyAutoGUI

import pyautogui
import time
import random


print(pyautogui.size())


while True:
    time.sleep(4)
    next_width =  random.randint(0, pyautogui.size().width)
    next_height =  random.randint(0, pyautogui.size().height)
    pyautogui.move(next_width, next_height, duration=2)
    print(next_width, next_height)
    
