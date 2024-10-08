# Selenium Irish Pronunciation Scraper

This script scrapes Irish word pronunciations from [Forvo](https://forvo.com) using Selenium. It logs the extracted words to a file named `found_words.log`.

### Requirements

- Python 3
- Selenium
- ChromeDriver (installed automatically with `webdriver_manager`)

### Installation

1. Install dependencies:
   ```sh
   pip install selenium webdriver-manager
   ```

### Usage

Run the script with the following options:

```sh
python scraper.py --start_page <start_page_number> --page_count <number_of_pages>
```

- `--start_page`: The page number to start scraping from (default: 1).
- `--page_count`: Number of pages to scrape (default: 1).

### Example

```sh
python scraper.py --start_page 1 --page_count 5
```

This will scrape 5 pages starting from page 1 and log the words found to `found_words.log`.

### Notes

- The script is configured to use Chrome and start in maximized mode.
- It uses a user-agent to mimic a standard browser.
- Ensure Chrome is installed on your machine.

Note: At the moment, the script can only scrape one page at a time.
