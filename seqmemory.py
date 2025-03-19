from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

#Color of center: (14,58,92)
tl = (1160, 675)
tm = (tl[0]+250, tl[1])
tr = (tl[0]+500, tl[1])
ml = (tl[0], tl[1]+250)
mm = (tl[0]+250, tl[1]+250)
mr = (tl[0]+500, tl[1]+250)
bl = (tl[0], tl[1]+500)
bm = (tl[0]+250, tl[1]+500)
br = (tl[0]+500, tl[1]+500)
moves = []

def record(moves):
    moves = []
    while True:
        if pyautogui.pixel(tl) == (8, 11, 12) and moves[-1] != tl:
            moves.append(tl)
        if pyautogui.pixel(tm) == (8, 11, 12) and moves[-1] != tm:
            moves.append(tm)
        if pyautogui.pixel(tr) == (8, 11, 12) and moves[-1] != tr:
            moves.append(tr)
        if pyautogui.pixel(ml) == (8, 11, 12) and moves[-1] != ml:
            moves.append(ml)
        if pyautogui.pixel(mm) == (8, 11, 12) and moves[-1] != mm:
            moves.append(mm)
        if pyautogui.pixel(mr) == (8, 11, 12) and moves[-1] != mr:
            moves.append(mr)
        if pyautogui.pixel(bl) == (8, 11, 12) and moves[-1] != bl:
            moves.append(bl)
        if pyautogui.pixel(bm) == (8, 11, 12) and moves[-1] != bm:
            moves.append(bm)
        if pyautogui.pixel(br) == (8, 11, 12) and moves[-1] != br:
            moves.append(br)
        if pyautogui.pixel(tl) == blue and pyautogui.pixel(tm) == blue and pyautogui.pixel(tr) == blue and pyautogui.pixel(ml) == blue and pyautogui.pixel(mm) == blue and pyautogui.pixel(mr) == blue and pyautogui.pixel(bl) == blue and pyautogui.pixel(bm) == blue and pyautogui.pixel(br) == blue:
            break    

    
def execute(moves):
    for i in moves:
        click(i)
        time.sleep(0.8)

def stop():
    if keyboard.is_pressed('space'):
        return True
    else:
        return False

while stop() == False:
    record(moves)
    time.sleep(1)
    execute(moves)
        

  
