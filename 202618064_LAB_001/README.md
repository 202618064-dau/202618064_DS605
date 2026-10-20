# DS605 Lab 1: Web Scraping, Data Preprocessing & Visualization


**Student:** Gauri Dawar  
**Student ID:** 202618064  
**Data Source:** [Books to Scrape](https://books.toscrape.com/)

## Overview

This project implements an end-to-end data pipeline using Python and Scrapy to collect book information, clean and transform the scraped data, and analyze patterns through visualizations. The project covers web scraping, data quality checks, feature engineering, exploratory data analysis (EDA), and insight generation.

## Tasks Completed

### Task 1 — Web Scraping
- Used Scrapy to scrape book details from catalog pages 20–25 and individual product pages.
- Extracted nine attributes: title, category, price, rating, availability, description, UPC, number of reviews, and product URL.
- Collected **120 book records** and exported the raw dataset to CSV.
- Verified dataset structure, missing values, and duplicate UPCs. The initial dataset had no missing values or duplicate UPCs.

### Task 2 — Data Preprocessing
- Removed extra spaces and duplicate records based on UPC.
- Handled missing values and converted prices and ratings into numeric formats.
- Engineered three features:
  - `description_length` — measures description length.
  - `price_category` — groups books by price.
  - `is_expensive` — identifies books meeting a price-based criterion.
- Saved the cleaned dataset as `books_cleaned.csv`.

### Tasks 3 & 4 — Visualization and Insights
- Generated visualizations for price distribution, rating distribution, category counts, description length versus price, and numerical correlations.
- Created a word cloud from book descriptions.
- Investigated the relationship between price and rating.
- Calculated `value_score = Rating / Price` to compare book ratings relative to price.

## Key Findings

- Book prices were concentrated mainly around the £40–£60 range, with books across a wider range of prices.
- The rating distribution included all five rating categories.
- The category chart showed nonfiction among the most represented categories, while poetry and art were among the least represented.
- Price and rating had an extremely weak linear correlation of **−0.038**, suggesting that higher prices do not necessarily correspond to higher ratings.
- Books priced around £10–£20 with ratings of four or five stars appeared to offer comparatively good value.
- The analysis is limited to a sample of 120 books, and findings may differ across other catalog pages or at later times.

## Technologies Used

- Python
- Scrapy
- Pandas and NumPy
- Matplotlib and Seaborn
- WordCloud
- Jupyter Notebook

## Project Structure

```text
202618064_LAB_001/
├── Task1_Scraping.ipynb
├── Task2_Preprocessing.ipynb
├── Task3&4_Visualization.ipynb
├── bookscraper/
│   ├── books_raw.csv
│   └── books_cleaned.csv
└── README.md
```

## Conclusion

This lab demonstrates a complete data pipeline, from automated web scraping to data cleaning, feature engineering, visualization, and interpretation. It highlights how structured data collected from the web can be transformed into useful insights while acknowledging the limitations of a small, time-sensitive sample.

