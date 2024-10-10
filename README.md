# Web Scraper with Selenium

A robust and scalable web scraping tool built with Python and Selenium, incorporating design patterns for maintainability and flexibility.

## Features

- **Singleton Logger**: Ensures consistent and centralized logging.
- **Factory Pattern**: Simplifies WebDriver creation and configuration.
- **Command Pattern**: Encapsulates scraping actions for modularity.
- **Configurable Scraping**: Specify start page and number of pages via command-line arguments.
- **Error Handling**: Gracefully manages timeouts and unexpected errors.

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/hafdon/forvo-selenium-chromedriver.git
   cd forvo-selenium-chromedriver
   ```

````

2. **Create a virtual environment and activate it**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the scraper with optional arguments:

```bash
python scraper.py --start_page 1 --page_count 5
```

- `--start_page`: Page number to start scraping from (default: 1)
- `--page_count`: Number of pages to scrape (default: 1)

## Logging

All found words are logged to `found_words.log` with timestamps and details.

## Project Structure

- `main.py`: Main script to execute the scraper.
- `Logger.py`: Singleton Logger implementation.
- `WebDriverFactory.py`: Factory for creating WebDriver instances.
- `ScraperCommand.py`: Command pattern implementation for scraping actions.
- `requirements.txt`: Python dependencies.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the [MIT License](LICENSE).
````
