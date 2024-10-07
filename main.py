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
import logging

# Configure logging
logging.basicConfig(
    filename="found_words.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def log_message(message):
    print(message)
    logging.info(message)


# Optional: Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
# chrome_options.add_argument("--headless")  # Uncomment to run in headless mode (no GUI)

# Setup ChromeDriver using webdriver_manager
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
# driver = webdriver.Chrome(service=service, options=chrome_options)
page_count = 2
start_page = 24
# end_page = 198
end_page = start_page + page_count - 1

# import threading``


def process_page(page_num, driver):
    try:
        url = f"https://forvo.com/languages-pronunciations/ga/page-{page_num}/"
        log_message(f"\nNavigating to: {url}")
        driver.get(url)

        try:
            WebDriverWait(driver, 2).until(
                lambda d: d.find_elements(By.CSS_SELECTOR, "a.word > span")
            )
        except TimeoutException:
            log_message(f"Timeout while waiting for elements on page {page_num}.")
            return

        try:
            span_elements = driver.find_elements(By.CSS_SELECTOR, "a.word > span")
            if not span_elements:
                log_message(f"No words found on page {page_num}.")
                return

            for idx, span in enumerate(span_elements, start=1):
                word = span.text.strip()
                log_entry = f"Page {page_num} - Word {idx}: {word}"
                log_message(log_entry)

        except Exception as e:
            log_message(f"Error extracting words on page {page_num}: {e}")
            return

        time.sleep(1)

    except KeyboardInterrupt:
        log_message("Script interrupted by user.")

    finally:
        driver.quit()
        log_message(
            f"Scraping completed for page {page_num}.",
        )


if __name__ == "__main__":
    # Open the log file in write mode to start fresh
    log_message("Found Words:\n")

    # threads = []

    driver_instance = webdriver.Chrome(service=service, options=chrome_options)
    for page_num in range(start_page, end_page + 1):
        #    driver_instance = webdriver.Chrome(service=service, options=chrome_options)
        # thread = threading.Thread(
        #     target=process_page, args=(page_num, driver_instance, log_file_path)
        # )

        process_page(page_num, driver_instance)
        # threads.append(thread)
        # thread.start()

    # for thread in threads:
    # thread.join()

    log_message(
        "All scraping tasks completed. All found words have been logged to 'found_words.log'."
    )
