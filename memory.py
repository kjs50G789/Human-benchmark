from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up a Selenium WebDriver instance for chrome
driver = webdriver.Chrome()

# Open the memory test page
memory_test_url = 'https://humanbenchmark.com/tests/memory'
driver.get(memory_test_url)

# Start
start_button = wait.until(
    EC.presence_of_element_located((By.XPATH, '//button[text()="Start"]'))
)
start_button.click()

# List to store the active squares
active_squares = []
x = 0

while True:
    # Find all active squares and store their elements + click
    start_time = time.time()
    polling_duration = 3
    print(f"checking...{x}")
    x+=1
    
    while time.time() - start_time < polling_duration:
        current_active_squares = driver.find_elements(
            By.CSS_SELECTOR, 'div.active.css-lxtdud.eut2yre1'
        )
        
        for square in current_active_squares:
            if square not in active_squares:
                active_squares.append(square)
    time.sleep(1)
    for square in active_squares:
        square.click()
    active_squares = []
    time.sleep(0.5)