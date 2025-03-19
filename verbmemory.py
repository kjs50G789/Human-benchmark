from PIL import Image
import pytesseract as tess
import pyautogui, keyboard, time, win32api, win32con, os

#gloabl
def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

list_of_words = []

time.sleep(2)
while keyboard.is_pressed('q') == False:
    #screenshot area
    x_ss, y_ss, height, width = 1009, 739, 878, 227
    screenshot = pyautogui.screenshot(region=(x_ss, y_ss, height, width))
    screenshot.save('screenshot.png')

    #get image text via ocr
    img = Image.open('screenshot.png')
    text = tess.image_to_string(img)
    print(text)

    #word check
    if text in list_of_words:
        click(1289,1024) #click seen
    else:
        list_of_words.append(text)
        click(1560,1024) #click new
    time.sleep(0.05)
