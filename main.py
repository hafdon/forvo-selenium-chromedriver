from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Use new headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/91.0.4472.124 Safari/537.36"
)

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the log file in append mode
log_file_path = "progress_log.txt"
with open(log_file_path, "a", encoding="utf-8") as log_file:
    try:
        # Iterate through all pages from 1 to 198
        for page_num in range(1, 199):
            url = f"https://forvo.com/languages-pronunciations/ga/page-{page_num}/"
            print(f"Processing Page {page_num}: {url}")
            log_file.write(f"Processing Page {page_num}: {url}\n")

            try:
                # Navigate to the page
                driver.get(url)

                # Optional: Take a screenshot for debugging
                # driver.save_screenshot(f"page_{page_num}.png")

                # Explicit wait: Wait until the <h1> element is present
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.TAG_NAME, "h1"))
                )

                # Retrieve and print the header text
                try:
                    header_element = driver.find_element(By.TAG_NAME, "h1")
                    header_text = header_element.text
                    print(f"Header Text: {header_text}")
                    log_file.write(f"Header Text: {header_text}\n")
                except NoSuchElementException:
                    print("Header <h1> not found.")
                    log_file.write("Header <h1> not found.\n")

                # Explicit wait: Wait until at least one span inside a.word is present
                try:
                    WebDriverWait(driver, 15).until(
                        EC.presence_of_element_located(
                            (By.CSS_SELECTOR, "a.word > span")
                        )
                    )
                except TimeoutException:
                    print(f"No span elements found on page {page_num}.")
                    log_file.write(f"No span elements found on page {page_num}.\n")
                    continue  # Skip to the next page

                # Locate all <span> elements within <a class="word">
                span_elements = driver.find_elements(By.CSS_SELECTOR, "a.word > span")

                if not span_elements:
                    print(f"No span elements found on page {page_num}.")
                    log_file.write(f"No span elements found on page {page_num}.\n")
                    continue  # Skip to the next page

                # Extract text from each span and write to log
                for idx, span in enumerate(span_elements, start=1):
                    word = span.text.strip()
                    if word:
                        print(f"Word {idx}: {word}")
                        log_file.write(f"Word {idx}: {word}\n")
                    else:
                        print(f"Word {idx}: [No text found]")
                        log_file.write(f"Word {idx}: [No text found]\n")

                # Optionally, add a short delay to mimic human browsing and avoid being blocked
                time.sleep(1)  # Adjust as needed

            except Exception as e:
                print(f"An error occurred on page {page_num}: {e}")
                log_file.write(f"An error occurred on page {page_num}: {e}\n")
                continue  # Proceed to the next page

    finally:
        # Close the browser after all operations
        driver.quit()
        print("Browser closed.")
        log_file.write("Browser closed.\n")
