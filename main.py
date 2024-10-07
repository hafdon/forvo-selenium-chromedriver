from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time

# Optional: Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
# chrome_options.add_argument("--headless")  # Uncomment to run in headless mode (no GUI)

# Setup ChromeDriver using webdriver_manager
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

# Define the range of pages you want to scrape
start_page = 3
end_page = 198

# Open the log file in write mode to start fresh
with open("found_words.log", "w", encoding="utf-8") as log_file:
    log_file.write("Found Words:\n")

try:
    for page_num in range(start_page, end_page + 1):
        url = f"https://forvo.com/languages-pronunciations/ga/page-{page_num}/"
        print(f"Navigating to: {url}")
        driver.get(url)

        # Optional: Wait for the page to load completely using explicit wait
        try:
            # Wait until the span elements within 'a.word' are present
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.word > span"))
            )
        except TimeoutException:
            print(
                f"Timeout while waiting for elements on page {page_num}. Skipping to next page."
            )
            continue  # Skip to the next page if elements aren't found

        # Retrieve all span elements that contain the words
        try:
            span_elements = driver.find_elements(By.CSS_SELECTOR, "a.word > span")
            if not span_elements:
                print(f"No words found on page {page_num}.")
                continue  # Skip to the next page if no words are found

            # Iterate through the list and log each word
            for idx, span in enumerate(span_elements, start=1):
                word = span.text.strip()
                print(f"Page {page_num} - Word {idx}: {word}")
                # log_file.write(f"Page {page_num} - Word {idx}: {word}\n")

        except Exception as e:
            print(f"Error extracting words on page {page_num}: {e}")
            continue  # Skip to the next page in case of any error

        # Optional: Polite delay to avoid overwhelming the server
        time.sleep(1)  # Sleep for 1 second between page requests

except KeyboardInterrupt:
    print("Script interrupted by user.")

finally:
    # Close the browser after all operations
    driver.quit()
    print("Scraping completed. All found words have been logged to 'found_words.log'.")
