
# Scraper Development Guide

This guide outlines the process for creating a new scraper for the Data Universe subnet.

## 1. Create a New Scraper File

- Create a new Python file in the `scraping` directory (e.g., `scraping/new_scraper.py`).
- Implement a new scraper class that inherits from `scraping.scraper.Scraper`.
- Implement the `scrape` and `validate` methods.

## 2. Update Enums

- Add a new entry to the `DataSource` enum in `common/data.py`.
- Add a new entry to the `ScraperId` enum in `scraping/scraper.py`.

## 3. Update Scraper Provider

- Import your new scraper class in `scraping/provider.py`.
- Add a new entry to the `DEFAULT_FACTORIES` dictionary in `scraping/provider.py`.

## 4. Update Scraping Configuration

- Add a new configuration block to `scraping/config/scraping_config.json` for your new scraper.

## Checklist

- [ ] New scraper file created in `scraping` directory.
- [ ] New scraper class inherits from `Scraper`.
- [ ] `scrape` and `validate` methods implemented.
- [ ] `DataSource` enum updated in `common/data.py`.
- [ ] `ScraperId` enum updated in `scraping/scraper.py`.
- [ ] `DEFAULT_FACTORIES` dictionary updated in `scraping/provider.py`.
- [ ] `scraping_config.json` updated with new scraper configuration.
