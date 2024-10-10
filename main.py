import argparse

from Logger import Logger
from ScraperCommand import ScraperCommand
from WebDriverFactory import WebDriverFactory


# Factory Pattern for WebDriver
# Scraper Command Pattern
# The Command Pattern is a behavioral design pattern
# that turns a request into a stand-alone object containing all information about the request.
if __name__ == "__main__":
    # Parse command-line arguments
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

        driver_instance = WebDriverFactory.create_driver()
        scraper = ScraperCommand(driver_instance)
        for page_num in range(start_page, end_page + 1):
            scraper.execute(page_num)

    except KeyboardInterrupt:
        Logger.log_message("Script interrupted by user.")
    except Exception as e:
        Logger.log_message(f"Unexpected error occurred: {e}")
    finally:
        driver_instance.quit()
        Logger.log_message(f"Scraping completed for pages {start_page} to {end_page}.")

    print(
        "All scraping tasks completed. All found words have been logged to 'found_words.log'."
    )
