from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
from numba import njit

@njit
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
click(0,322)
while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(0,322)[1] == 205:
        click(0,322)
