import argparse
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

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


# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)


# Setup ChromeDriver using webdriver_manager
service = Service(ChromeDriverManager().install())


def process_page(page_num, driver):
    url = f"https://forvo.com/languages-pronunciations/ga/page-{page_num}/"
    log_message(f"\nNavigating to: {url}")
    driver.get(url)

    try:

        WebDriverWait(driver, 5).until(
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


if __name__ == "__main__":
    # Define command-line arguments
    parser = argparse.ArgumentParser(description="Web scraping with Selenium.")
    parser.add_argument(
        "--start_page", type=int, default=1, help="Page number to start scraping from."
    )
    parser.add_argument(
        "--page_count", type=int, default=1, help="Number of pages to scrape."
    )
    args = parser.parse_args()

    # Set start page and page count from command-line arguments
    start_page = args.start_page
    page_count = args.page_count
    end_page = start_page + page_count - 1

    try:

        driver_instance = webdriver.Chrome(service=service, options=chrome_options)
        for page_num in range(start_page, end_page + 1):

            process_page(page_num, driver_instance)
    except KeyboardInterrupt:
        log_message("Script interrupted by user.")

    finally:
        driver_instance.quit()
        log_message(
            f"Scraping completed for page {page_num}.",
        )

    print(
        "All scraping tasks completed. All found words have been logged to 'found_words.log'."
    )

