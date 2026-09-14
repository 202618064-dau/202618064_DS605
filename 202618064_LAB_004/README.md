# 🏠 Airbnb Price Prediction

## DS605 – Fundamentals of Machine Learning | Lab Assignment 4

### Live Dashboard Link - 

An end-to-end machine learning project for predicting the nightly price of
Airbnb listings in New York City using the Kaggle Airbnb Open Data dataset.

---

## 📌 Project Objective

The objective of this project is to build a complete machine learning workflow
for Airbnb price prediction, including data preparation, feature engineering,
model comparison, hyperparameter tuning, evaluation, and deployment through a
Streamlit web application.

---

## 📊 Dataset

**Dataset:** New York City Airbnb Open Data (`AB_NYC_2019.csv`)

The dataset contains information about Airbnb listings, including location,
room type, minimum nights, reviews, availability, and price.

---

## 🔍 Data Preparation

The following preprocessing steps were performed:

- Removed invalid zero-price listings.
- Removed extreme upper-tail prices above the 99th percentile.
- Handled missing values.
- Dropped `last_review` due to substantial missingness.
- Filled missing `reviews_per_month` with 0.
- Removed identifier and high-cardinality text features.
- Retained detailed neighbourhood information.
- Applied log transformation to `minimum_nights`.
- Applied scaling to numerical features.
- Applied one-hot encoding to categorical features.

---

## 🤖 Models Compared

Three regression models were evaluated:

| Model | Test MAE | Test RMSE | Test R² |
|---|---:|---:|---:|
| Linear Regression | 49.94 | 79.61 | 0.4175 |
| Random Forest | 44.93 | 72.91 | 0.5115 |
| Gradient Boosting | 46.38 | 75.51 | 0.4760 |

### Final Model

The **Tuned Random Forest Regressor** was selected as the final model.

**Final Test Performance:**

- MAE: **43.82**
- RMSE: **71.81**
- R²: **0.5261**

Hyperparameter tuning reduced overfitting and improved test performance.

---

## ⚙️ Final Machine Learning Pipeline

The final workflow combines preprocessing and the tuned Random Forest model
into a single pipeline.

```text
Raw Airbnb Input
       ↓
ColumnTransformer
       ↓
Numerical Scaling
       ↓
Log Transformation
       ↓
One-Hot Encoding
       ↓
Tuned Random Forest
       ↓
Estimated Nightly Price