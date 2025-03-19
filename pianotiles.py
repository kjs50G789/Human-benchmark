from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

#Tile 1 720,1370 
#Tile 2 890,1380
#Tile 3 1090,1370
#Tile 4 1240,1380

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

while keyboard.is_pressed('q') == False:
    if pyautogui.pixel(720,800) == (0,0,0):
        click(720,800)
    if pyautogui.pixel(890,800) == (0,0,0):
        click(890,800)
    if pyautogui.pixel(1090,800) == (0,0,0):
        click(1090,800)
    if pyautogui.pixel(1240,800) == (0,0,0):
        click(1240,800)

