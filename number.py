from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up a Selenium WebDriver instance for chrome
driver = webdriver.Chrome()

# Open the Number Memory test
url = 'https://humanbenchmark.com/tests/number-memory'
driver.get(url)

# Wait for elements to load
wait = WebDriverWait(driver, 1000000000000000)  # Explicit wait with a 10-second timeout

# Click the start button to begin the test
start_button = wait.until(
    EC.presence_of_element_located((By.XPATH, '//button[text()="Start"]'))
)
start_button.click()

# Function to handle one round of the Number Memory test
def complete_round():
    # Find the big number and memorize it
    number_element = wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, 'big-number'))
    )
    number_to_memorize = number_element.text  # Retrieve the number
    print("Number to memorize:", number_to_memorize)

    # Find the input field and enter the memorized number
    input_field = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, 'input'))
    )
    input_field.send_keys(number_to_memorize)  # Enter the memorized number
    input_field.send_keys("\n")  # Submit the answer

    # Proceed to the next round
    next_button = wait.until(
        EC.presence_of_element_located((By.XPATH, '//button[text()="NEXT"]'))
    )
    next_button.click()  # Next round

# Loop through the Number Memory rounds
rounds = 1000  # How many rounds to complete
for _ in range(rounds):
    complete_round()