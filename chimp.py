from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Selenium WebDriver for chrome
driver = webdriver.Chrome()

# Navigate to test page
chimp_test_url = 'https://humanbenchmark.com/tests/chimp'
driver.get(chimp_test_url)

# Click "Start Test" to begin
start_button = wait.until(
    EC.presence_of_element_located((By.XPATH, '//button[text()="Start Test"]'))
)
start_button.click()

# Click the numbers in order
def click_numbers_in_order(max_number):
    for num in range(1, max_number + 1):
        # Locate the element with the specific `data-cellnumber`
        element = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, f'div[data-cellnumber="{num}"]'))
        )
        element.click()  # Click the number
    continue_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Continue"]'))
    )
    continue_button.click()

# Start with 1 to 4
for i in range(4, 41):
    click_numbers_in_order(i)