from Logger import Logger


from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class WebDriverFactory:
    @staticmethod
    def create_driver():
        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument(
            "--start-maximized"
        )  # Open browser in maximized mode
        chrome_options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        )
        # Setup ChromeDriver using webdriver_manager
        service = Service(ChromeDriverManager().install())
        try:
            driver = webdriver.Chrome(service=service, options=chrome_options)
            return driver
        except WebDriverException as e:
            Logger.log_message(f"Error creating WebDriver: {e}")
            raise  # re-raise the exception to be handled appropriately by the caller.
