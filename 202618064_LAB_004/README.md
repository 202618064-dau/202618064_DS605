# 🏠 Airbnb Price Prediction

## DS605 – Fundamentals of Machine Learning | Lab Assignment 4

An end-to-end machine learning project for predicting the nightly price of Airbnb listings in New York City using the Kaggle **AB_NYC_2019** dataset.

## 🚀 Live Application

🔗 **Streamlit App:**  
https://202618064ds605-2l7bc4enqzj4admql2tnc4.streamlit.app/

---

## 📊 Project Overview

The project follows a complete machine learning workflow:

- Data cleaning and missing-value handling
- Outlier treatment
- Exploratory data analysis
- Feature selection and engineering
- Data preprocessing
- Regression model comparison
- Hyperparameter tuning
- Final model evaluation
- Streamlit application development
- Online deployment

---

## 🧹 Data Preparation

Key preprocessing decisions:

- Removed invalid listings with `price = 0`
- Removed extreme prices above the 99th percentile
- Filled missing `reviews_per_month` values with `0`
- Removed `last_review`
- Filled missing text values with `"Unknown"`
- Removed high-cardinality identifiers such as `id` and `host_id`
- Applied `log1p` transformation to `minimum_nights`
- Applied one-hot encoding to categorical features
- Standardized numerical features

After outlier treatment, the dataset contained **48,410 listings**.

---

## 🤖 Model Comparison

Three regression models were evaluated:

| Model | Test MAE | Test RMSE | Test R² |
|---|---:|---:|---:|
| Linear Regression | $49.94 | $79.61 | 0.4175 |
| Random Forest | $44.93 | $72.91 | 0.5115 |
| Gradient Boosting | $46.38 | $75.51 | 0.4760 |

Random Forest produced the best initial performance but showed overfitting.

Hyperparameter tuning was therefore performed using `RandomizedSearchCV`.

### Final Model

**Tuned Random Forest Regressor**

- `n_estimators = 150`
- `max_depth = 15`
- `min_samples_split = 10`
- `min_samples_leaf = 2`
- `max_features = 0.5`

### Final Performance

| Metric | Test Result |
|---|---:|
| MAE | **$43.82** |
| RMSE | **$71.81** |
| R² | **0.5261** |

The tuned model reduced overfitting and improved test-set performance.

---

## 🌐 Streamlit Application

The application accepts Airbnb listing information including:

- Neighbourhood group
- Neighbourhood
- Latitude and longitude
- Room type
- Minimum nights
- Number of reviews
- Reviews per month
- Host listing count
- Availability

It then returns an estimated nightly Airbnb price.

The saved preprocessing and model are combined into a single pipeline to ensure consistent processing of new inputs.

---
Gauri Dawar
202618064
