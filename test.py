import keyboard, pyautogui
from PIL import Image
import pytesseract as tess
custom = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789'
img = Image.open('screenshot.png')
number = tess.image_to_string(img)
print(number)
