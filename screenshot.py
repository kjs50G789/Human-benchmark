import keyboard, pyautogui
while True:
    if keyboard.is_pressed('q') == True:
        x_ss, y_ss, height, width = 505, 391, 2027, 312
        screenshot = pyautogui.screenshot(region=(x_ss, y_ss, height, width))
        screenshot.save('screenshot.png')
        break
