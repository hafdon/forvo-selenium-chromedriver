from Logger import Logger
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium_stealth import stealth


class WebDriverFactory:
    @staticmethod
    def create_driver():
        try:
            # Configure Chrome options
            chrome_options = Options()
            # Open browser in maximized mode
            chrome_options.add_argument("--start-maximized")
            # Set a realistic User-Agent
            chrome_options.add_argument(
                "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            )
            # Disable automation flags to evade detection
            chrome_options.add_argument("--disable-blink-features=AutomationControlled")
            chrome_options.add_experimental_option(
                "excludeSwitches", ["enable-automation"]
            )
            chrome_options.add_experimental_option("useAutomationExtension", False)

            # Setup ChromeDriver using webdriver_manager
            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)

            # Apply selenium-stealth
            stealth(
                driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
                run_on_insecure_origins=False,
            )

            # Optional: Set window size and position if needed
            driver.set_window_position(0, 0)
            driver.set_window_size(1920, 1080)

            return driver

        except WebDriverException as e:
            Logger.log_message(f"Error creating WebDriver: {e}")
            raise  # re-raise the exception to be handled appropriately by the caller.
