from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException,
    TimeoutException,
    WebDriverException,
)
import time

# Optional: Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
# chrome_options.add_argument("--headless")  # Uncomment to run in headless mode (no GUI)

# Setup ChromeDriver using webdriver_manager
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)
page_count = 2

drivers = [
    webdriver.Chrome(service=service, options=chrome_options) for _ in range(page_count)
]


# Define the range of pages you want to scrape
start_page = 10
# end_page = 198
end_page = start_page + page_count - 1

# Path to the log file
log_file_path = "found_words.log"


# Function to log messages to both console and file
def log_message(message, log_file):
    print(message)
    log_file.write(message + "\n")


# Function to detect CAPTCHA presence
def is_captcha_present(driver):
    try:
        # Common CAPTCHA iframe (e.g., reCAPTCHA)
        driver.find_element(By.XPATH, "//iframe[contains(@src, 'captcha')]")
        return True
    except NoSuchElementException:
        pass

    try:
        # Look for CAPTCHA divs or other indicators
        driver.find_element(By.XPATH, "//div[contains(@class, 'captcha')]")
        return True
    except NoSuchElementException:
        pass

    # Add more detection logic if necessary
    # Example: Check for specific text that appears with CAPTCHA
    try:
        driver.find_element(By.XPATH, "//*[contains(text(), 'verify you are human')]")
        return True
    except NoSuchElementException:
        pass

    return False


# Open the log file in write mode to start fresh
with open(log_file_path, "w", encoding="utf-8") as log_file:
    log_file.write("Found Words:\n")

    try:
        for page_num, driver in enumerate(drivers, start=start_page):

            url = f"https://forvo.com/languages-pronunciations/ga/page-{page_num}/"
            log_message(f"\nNavigating to: {url}", log_file)
            driver.get(url)

            try:
                WebDriverWait(driver, 5).until(
                    lambda d: d.find_elements(By.CSS_SELECTOR, "a.word > span")
                )
            except TimeoutException:
                log_message(
                    f"Timeout while waiting for elements on page {page_num}.",
                    log_file,
                )
                continue  # Skip to the next page if elements aren't found

            try:
                span_elements = driver.find_elements(By.CSS_SELECTOR, "a.word > span")
                if not span_elements:
                    log_message(f"No words found on page {page_num}.", log_file)
                    continue  # Skip to the next page if no words are found

                for idx, span in enumerate(span_elements, start=1):
                    word = span.text.strip()
                    log_entry = f"Page {page_num} - Word {idx}: {word}"
                    log_message(log_entry, log_file)

            except Exception as e:
                log_message(f"Error extracting words on page {page_num}: {e}", log_file)
                continue  # Skip to the next page in case of any error

            time.sleep(1)

    except KeyboardInterrupt:
        log_message("Script interrupted by user.", log_file)

    finally:
        # Close the browser after all operations
        driver.quit()
        log_message(
            "Scraping completed. All found words have been logged to 'found_words.log'.",
            log_file,
        )
