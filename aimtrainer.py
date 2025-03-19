from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Color of center: (9,55,91)
while keyboard.is_pressed('q') == False:
    flag = 0
    pic = pyautogui.screenshot(region=(0,443,2833,952))

    width, height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):

            r, g, b = pic.getpixel((x, y))

            if r == 9 and g == 55 and b == 91:
                flag = 1
                click(x, y+443)
                time.sleep(0.08)
                break

        if flag == 1:
            break
