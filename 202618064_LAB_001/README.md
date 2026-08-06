# DS605 Lab 1 – Web Scraping, Data Preprocessing and Visualization

## Overview

This repository contains the solution for **DS605 Lab 1**, which demonstrates the complete data analysis workflow using Python. The project involves scraping book data from an e-commerce website, cleaning and preprocessing the collected data, performing feature engineering, visualizing the data, and extracting meaningful insights.

## Dataset Source

Website: http://books.toscrape.com/

The dataset was created by scraping book information from the website using Scrapy.

---

## Project Structure

```
202618064_LAB_001/
│
├── bookscraper/
│   ├── spiders/
│   ├── items.py
│   ├── pipelines.py
│   ├── settings.py
│   └── ...
│
├── Task1_Scraping.ipynb
├── Task2_Preprocessing.ipynb
├── Task3&4_Visualization.ipynb
└── README.md
```

---

## Tasks Completed

### Task 1 – Web Scraping

- Scraped book information using Scrapy
- Collected the following attributes:
  - Title
  - Price
  - Rating
  - Stock Availability
  - Category
  - Product Description
  - UPC
- Handled pagination to scrape multiple pages
- Exported the scraped data into CSV format

---

### Task 2 – Data Preprocessing

- Removed duplicate records
- Handled missing values
- Converted price into numeric format
- Converted ratings into numerical values
- Extracted stock quantity
- Cleaned textual data
- Performed feature engineering by creating:
  - Description Length
  - Value Score

---

### Task 3 – Data Visualization

Generated the following visualizations:

- Distribution of Book Prices
- Distribution of Book Ratings
- Top Book Categories
- Description Length vs Price
- Correlation Heatmap
- Average Book Price by Rating
- Best Value Books (Bubble Chart)
- Word Cloud of Book Descriptions

---

### Task 4 – Insights and Interpretation

The analysis includes:

- Price distribution analysis
- Rating distribution analysis
- Category distribution analysis
- Relationship between description length and price
- Correlation among numerical features
- Relationship between price and rating
- Identification of best value books
- Dataset limitations
- Overall conclusion

---

## Technologies Used

- Python
- Scrapy
- Pandas
- NumPy
- Matplotlib
- Seaborn
- WordCloud
- Jupyter Notebook

---

## Key Findings

- Book prices range approximately from **£10 to £60**.
- Ratings are distributed fairly evenly across all categories.
- No significant relationship exists between book price and rating.
- Nonfiction is the most represented category in the scraped dataset.
- Books with higher ratings and lower prices provide better value for money.
- Correlation analysis indicates very weak relationships among price, rating, and description length.

---

## How to Run

1. Clone the repository.

```bash
git clone https://github.com/202618064-dau/202618064_DS605.git
```

2. Navigate to the project folder.

```bash
cd 202618064_LAB_001
```

3. Install the required libraries.

```bash
pip install scrapy pandas numpy matplotlib seaborn wordcloud
```

4. Run the notebooks in order:

- Task1_Scraping.ipynb
- Task2_Preprocessing.ipynb
- Task3&4_Visualization.ipynb

---

## Repository

GitHub Repository:

https://github.com/202618064-dau/202618064_DS605

---

## Author

**Name:** Gauri Dawar

**Course:** DS605 – Data Science Lab

**University:** CHRIST (Deemed to be University)