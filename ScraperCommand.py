from Logger import Logger
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import random
import time


class ScraperCommand:
    def __init__(self, driver):
        self.driver = driver

    def execute(self, page_num):
        url = f"https://forvo.com/languages-pronunciations/ga/page-{page_num}/"
        Logger.log_message(f"Navigating to {url}")
        self.driver.get(url)

        try:
            WebDriverWait(self.driver, 5).until(
                lambda d: d.find_elements(By.CSS_SELECTOR, "a.word > span")
            )
        except TimeoutException:
            Logger.log_message(
                f"Timeout while waiting for elements on page {page_num}."
            )
            return

        try:
            span_elements = self.driver.find_elements(By.CSS_SELECTOR, "a.word > span")
            if not span_elements:
                Logger.log_message(f"No words found on page {page_num}.")
                return

            for idx, span in enumerate(span_elements, start=1):
                word = span.text.strip()
                log_entry = f"Page {page_num} - Word {idx}: {word}"
                Logger.log_message(log_entry)

        except Exception as e:
            Logger.log_message(f"Error extracting words on page {page_num}: {e}")
            return

        time.sleep(random.uniform(2, 5))
