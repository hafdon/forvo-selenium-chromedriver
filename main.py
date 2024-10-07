from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# Optional: Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
# chrome_options.add_argument("--headless")  # Uncomment to run in headless mode (no GUI)

# Setup ChromeDriver using webdriver_manager
service = Service(ChromeDriverManager().install())

# Initialize WebDriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to a webpage
    driver.get("https://forvo.com/languages-pronunciations/ga/page-1/")
    # ... https://forvo.com/languages-pronunciations/ga/page-198/

    # Optional: Wait for the page to load completely
    driver.implicitly_wait(
        10
    )  # Waits up to 10 seconds for elements to become available

    # Print the title of the page
    print("Page Title:", driver.title)

    # Example: Find an element by its tag name and print its text
    element = driver.find_element("tag name", "h1")
    print("Header Text:", element.text)

    # Method 1: Using CSS Selector
    try:
        span_elements = driver.find_elements(By.CSS_SELECTOR, "a.word > span")
        # Iterate through the list and print each word
        for idx, span in enumerate(span_elements, start=1):
            print(f"Word {idx}: {span.text}")
    except Exception as e:
        print("Error using CSS Selector:", e)

finally:
    # Close the browser after the operations
    driver.quit()
