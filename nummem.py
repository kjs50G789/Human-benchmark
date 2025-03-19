from PIL import Image
import pytesseract as tess
import pyautogui, keyboard, time, win32api, win32con

time.sleep(1)
while keyboard.is_pressed('q') == False:
    #screenshot area
    x_ss, y_ss, height, width = 505, 391, 2027, 312
    screenshot = pyautogui.screenshot(region=(x_ss, y_ss, height, width))
    screenshot.save('screenshot.png')

    #get image text via ocr
    img = Image.open('screenshot.png')
    number = tess.image_to_string(img)
    print(number)

    if pyautogui.pixel(2254, 863) == (38, 82, 150):
        #type number
        pyautogui.typewrite(number)
        keyboard.press('enter')
        keyboard.release('enter')
        time.sleep(0.05)
        keyboard.press('enter')
        keyboard.release('enter')
        time.sleep(0.05)
