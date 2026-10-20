# DS605 Lab 3: Data Preprocessing and Model Performance Evaluation

**Name: Gauri Dawar**

**ID: 202618064**


## Overview

This lab explores how data preprocessing techniques affect machine learning model performance using **Scikit-learn**. The project uses a hotel booking dataset to predict whether a hotel reservation will be canceled.

Two preprocessing pipelines are developed and compared:

- **Pipeline A:** KNN imputation, StandardScaler, and OneHotEncoder.
- **Pipeline B:** KNN imputation, MinMaxScaler, and OneHotEncoder.

Logistic Regression and Decision Tree classifiers are trained with both pipelines, and their performance is evaluated using multiple classification metrics.

## Objectives

- Load and explore a real-world dataset using Pandas.
- Identify missing values, data leakage, and extreme outliers.
- Build preprocessing pipelines using `Pipeline` and `ColumnTransformer`.
- Handle numerical and categorical features appropriately.
- Compare StandardScaler and MinMaxScaler.
- Train Logistic Regression and Decision Tree classifiers.
- Evaluate models using accuracy, precision, recall, F1-score, and confusion matrices.
- Identify the best-performing preprocessing and model combination.

## Dataset

**Dataset:** `hotel_bookings.csv`

The dataset contains hotel reservation information, including booking lead time, length of stay, number of guests, average daily rate, customer type, and other booking-related attributes.

**Target variable:** `is_canceled`

- `0` — Booking was not canceled.
- `1` — Booking was canceled.

The task is a **binary classification problem**.

## Project Workflow

### Part A — Data Loading and Preprocessing

#### 1. Data Exploration

- Loaded the dataset using Pandas.
- Examined the dataset's shape, data types, summary statistics, and target class distribution.
- Separated the target variable (`is_canceled`) from the input features.
- Identified numerical and categorical columns.

#### 2. Missing-Value Handling

The missing-value analysis identified `company` as a highly incomplete feature, with approximately **94.31% missing values**.

- Dropped `company` because of its extremely high missingness.
- Retained other features with missing values for appropriate imputation.
- Used `KNNImputer` with five neighbors for numerical features.
- Used `SimpleImputer(strategy="most_frequent")` for categorical features.

#### 3. Data Leakage Prevention

Removed the following columns:

- `reservation_status`
- `reservation_status_date`

These features can reveal information about the booking outcome after it occurs. Keeping them could lead to misleadingly high performance and poor real-world generalization.

#### 4. Outlier Detection and Treatment

Used boxplots to inspect selected numerical features, including `adr`, `lead_time`, and length-of-stay variables.

Extreme values were filtered using the **Interquartile Range (IQR) method with a multiplier of 3**, focusing on unusually extreme observations rather than aggressively removing natural variation.

After cleaning, the dataset contained **87,289 rows and 28 input features**, excluding the target variable.

#### 5. Train-Test Split

The data was split using an 80:20 train-test split with stratification on `is_canceled` and `random_state=42`.

Stratification helps preserve the target class distribution in both sets.

### Part B — Preprocessing Pipelines

Two pipelines were created to compare numerical scaling methods while keeping the remaining preprocessing steps consistent.

| Processing step | Pipeline A | Pipeline B |
|---|---|---|
| Numerical missing values | KNNImputer, 5 neighbors | KNNImputer, 5 neighbors |
| Numerical scaling | StandardScaler | MinMaxScaler |
| Categorical missing values | Most frequent value | Most frequent value |
| Categorical encoding | OneHotEncoder | OneHotEncoder |

**StandardScaler** standardizes numerical features to have a mean of approximately zero and a standard deviation of one.

**MinMaxScaler** scales numerical features to a fixed range, by default between zero and one.

`ColumnTransformer` applies the appropriate transformations to each feature type, while `Pipeline` combines preprocessing and model training into a single workflow.

Fitting the pipelines on training data and applying the learned transformations to test data helps prevent preprocessing data leakage.

### Part C — Model Training and Evaluation

Two classification algorithms were evaluated:

1. Logistic Regression
2. Decision Tree Classifier

Each classifier was combined with both preprocessing pipelines, resulting in four model-pipeline combinations.

The evaluation metrics were:

- **Accuracy:** Overall proportion of correct predictions.
- **Precision:** Proportion of predicted cancellations that were actual cancellations.
- **Recall:** Proportion of actual cancellations correctly identified.
- **F1-score:** Harmonic mean of precision and recall.
- **Confusion matrix:** Breakdown of correct and incorrect predictions for each class.

Training accuracy was also compared with test accuracy to identify possible overfitting.

## Results and Observations

The notebook's reported results are summarized below.

| Model and preprocessing | Test accuracy | F1-score |
|---|---:|---:|
| Logistic Regression + StandardScaler | 81.31% | 0.744 |
| Logistic Regression + MinMaxScaler | 80.83% | 0.737 |
| Decision Tree + StandardScaler | 85.63% | 0.819 |
| Decision Tree + MinMaxScaler | 85.62% | Approximately 0.819 |

*Values are reported from the notebook's observations and may be rounded.*

### Key Findings

- **Best overall combination:** Decision Tree with Pipeline A (StandardScaler), with 85.63% test accuracy and an F1-score of 0.819.
- **Effect on Logistic Regression:** StandardScaler performed slightly better than MinMaxScaler.
- **Effect on Decision Tree:** The choice of scaler had almost no impact on test performance.
- **Overfitting:** The Decision Tree's substantially higher training accuracy than test accuracy suggests possible overfitting.
- **Importance of preprocessing:** Correctly handling missing values, categorical variables, extreme values, and data leakage is essential for a meaningful model comparison.

## Technologies Used

- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook

## Project Structure

```text
202618064_LAB_003/
├── 202618064_lab3.ipynb
├── hotel_bookings.csv
└── README.md
```


## Conclusion

This lab demonstrates how preprocessing decisions influence classification performance. Comparing StandardScaler and MinMaxScaler showed that the scaling method affected Logistic Regression slightly but had virtually no effect on the Decision Tree.

Among the four tested combinations, **Decision Tree with StandardScaler achieved the best reported test accuracy and F1-score**. Its train-test performance gap also highlighted the importance of checking for overfitting rather than relying on test accuracy alone.

Overall, the experiment emphasizes the importance of building reliable preprocessing pipelines, preventing data leakage, and evaluating models using multiple performance metrics.

