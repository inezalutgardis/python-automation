# 📰 News Scraper

News Scraper is a simple Python script that scrapes the latest headlines from BBC News and saves them into a CSV file.  

This project demonstrates web scraping, automation, and data handling with Python.

## Features
- Fetches BBC News homepage headlines (`h1`, `h2`, `h3` tags).
- Filters out duplicates and junk text.
- Saves results into a timestamped CSV file.
- Example output included (`sample_output.csv`).

## Requirements
- Python 3.x
- Libraries: `requests`, `beautifulsoup4`, `pandas`, `lxml`

Install dependencies:
```bash
pip install -r requirements.txt
