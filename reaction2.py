import pyautogui
import time
import webbrowser

url = 'https://humanbenchmark.com/tests/reactiontime'

# Open Website on Windows
webbrowser.open(url)

# Click to Start
pyautogui.moveTo(320, 400)  # Adjust coordinates as needed
time.sleep(2)  # Wait for page to load
pyautogui.click()

num_times = 0

while True:
    # Get the color of the pixel at the given coordinates
    pixel_color = pyautogui.pixel(320, 400)  # Adjust coordinates as needed

    # Click when the green component of the color is greater than 150
    if pixel_color[1] > 120:  # The second item in the tuple is the green component
        pyautogui.click()

        num_times += 1
        if num_times == 5:
            # Test runs 5 times
            break

        # Click to start again
        time.sleep(1)
        pyautogui.click()
