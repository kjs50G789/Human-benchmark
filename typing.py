import os
import pyautogui
import subprocess
import time
import webbrowser

url = 'https://humanbenchmark.com/tests/typing'

# Open the URL
webbrowser.open(url)
time.sleep(5)

def type_fast():
    # Define the coordinates for the screenshot
    screenshot_region = (348, 485, 1192, 175)  # Adjust coordinates if needed

    # Take a screenshot of text
    pyautogui.screenshot('text.png', region=screenshot_region)

    # Try running Tesseract OCR on the screenshot
    try:
        subprocess.run(['tesseract', 'text.png', 'text-result', '--dpi', '150'], check=True)
    except FileNotFoundError:
        print("Error: Tesseract OCR is not found. Please ensure it's installed and in PATH.")
        return
    except subprocess.CalledProcessError as e:
        print("Error running Tesseract OCR:", e)
        return

    # Read and process the text result
    try:
        with open('text-result.txt', 'r') as file:
            data = file.read().replace('\n', ' ')
        
        # Cleanup
        if data.startswith('|') or data.startswith('['):
            data = data[1:]

        data = data.replace('|', 'I').strip()
        
        print("Extracted TEXT:", data)

        # Click inside the typing box and type
        pyautogui.moveTo(1062, 512)  # Adjust coordinates if needed
        pyautogui.click()
        pyautogui.write(data, interval=0)

        # Cleanup
        os.remove('text.png')
        os.remove('text-result.txt')
    
    except FileNotFoundError as e:
        print("Error: Resulting text file not found.", e)

    # Final move for visual indication
    pyautogui.moveTo(100, 100)

type_fast()
