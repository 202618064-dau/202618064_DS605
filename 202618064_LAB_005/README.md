# DS605 Lab 5: Regression, Classification and Feature Engineering

**Name: Gauri Dawar**
**ID: 202618064**

## Overview

This lab explores regression and classification using the Garments Worker Productivity dataset. It compares Scikit-learn implementations with models implemented manually using NumPy and investigates how preprocessing, optimization settings, and feature selection affect model performance.

The notebook includes exploratory data analysis, data cleaning, train-test splitting, categorical encoding, missing-value imputation, feature scaling, model evaluation, and optimization experiments.

## Objectives

- Explore the dataset and understand its numerical and categorical features.
- Handle missing values and clean categorical data.
- Create a binary classification target from actual and targeted productivity.
- Build regression and classification models using Scikit-learn.
- Implement Linear Regression and Logistic Regression from scratch using NumPy.
- Evaluate models using appropriate regression and classification metrics.
- Investigate learning-rate changes, missingness indicators, and feature selection.
- Compare model performance and identify the best-performing configuration among the experiments.

## Dataset

**Dataset:** Garments Worker Productivity

The dataset contains information about garment-production teams, including productivity targets, actual productivity, work-in-progress (WIP), department, quarter, day, and other production-related attributes.

The notebook loads the dataset from:

```text
garments_worker_productivity.csv
```

## Exploratory Data Analysis

The initial analysis examines:

- Dataset structure, data types, and summary statistics.
- Missing-value counts and their distribution across departments.
- Unique values and frequencies of categorical features.
- WIP statistics and actual versus targeted productivity.
- Class proportions for the derived classification target.

This analysis helps identify missing data, categorical inconsistencies, and potential preprocessing requirements.

## Data Cleaning and Feature Engineering

The notebook performs the following operations:

- Removes unnecessary whitespace from department labels.
- Extracts month and day-of-month features from the date.
- Creates a binary target named `MeetsTarget`, which equals 1 when actual productivity meets or exceeds targeted productivity, and 0 otherwise.
- Separates regression and classification targets.
- Uses a reproducible train-test split.
- Checks that training and testing indices do not overlap.

Missing WIP values are handled using the median calculated from the training data. This prevents preprocessing statistics from being learned from the test set.

## Part A: Scikit-learn Implementations

### Linear Regression

Linear Regression predicts the continuous `actual_productivity` target.

| Metric | Test result |
|---|---:|
| MAE | 0.1083 |
| RMSE | 0.1451 |
| R² | 0.2754 |

The model provides a baseline for predicting actual productivity. Its R² indicates that the model explains a limited proportion of the variation in the target, leaving room for further improvement.

### Logistic Regression

Logistic Regression predicts the binary `MeetsTarget` target.

| Metric | Test result |
|---|---:|
| Accuracy | 69.58% |
| Precision | 75.00% |
| Recall | 87.43% |
| F1-score | 80.74% |

The model achieves relatively high recall, meaning it identifies a large proportion of the positive class. Precision and recall together provide a more complete picture than accuracy alone.

## Part B: Manual Implementations Using NumPy

### Manual Linear Regression

Linear Regression is implemented using the Moore–Penrose pseudoinverse:

\[
\beta = X^+y
\]

An intercept column is added to the feature matrix, and regression metrics are calculated manually.

The manual implementation reproduces the Scikit-learn results:

| Metric | Test result |
|---|---:|
| MAE | 0.1083 |
| RMSE | 0.1451 |
| R² | 0.2754 |

The matching results verify that the pseudoinverse implementation produces the same regression solution for the processed dataset.

### Manual Logistic Regression

Logistic Regression is implemented from scratch using:

- The sigmoid function.
- Binary Cross-Entropy loss.
- Gradient calculation and gradient descent.
- A classification threshold of 0.5.
- Manually calculated accuracy, precision, recall, and F1-score.

The baseline manual model uses a learning rate of 0.1 and 1,000 iterations.

| Metric | Test result |
|---|---:|
| Accuracy | 70.42% |
| Precision | 75.24% |
| Recall | 88.57% |
| F1-score | 81.36% |

The manual implementation produces results close to the Scikit-learn baseline, although exact equality is not expected because the optimization procedures differ.

## Optimization Experiments

### 1. Learning-rate adjustment

The learning rate was increased from 0.1 to 0.3.

Training loss decreased and training accuracy improved, but the test metrics remained unchanged. Therefore, the higher learning rate did not provide an observed improvement in test-set performance.

### 2. WIP missingness indicator

An additional `wip_missing` feature was introduced to indicate whether the original WIP value was missing.

The feature did not improve the test results:

| Metric | Baseline | With indicator |
|---|---:|---:|
| Accuracy | 70.42% | 69.58% |
| Recall | 88.57% | 86.86% |
| F1-score | 81.36% | 80.64% |

The indicator was not retained in the final candidate because it reduced the observed test performance.

### 3. Feature selection

Feature selection was performed using correlations calculated from the training data. Three numerical features were removed, reducing the numerical feature count from 12 to 9.

The resulting processed feature count decreased from 25 to 22.

| Metric | Baseline manual Logistic Regression | Feature-selected model |
|---|---:|---:|
| Features | 25 | 22 |
| Accuracy | 70.42% | 72.08% |
| Precision | 75.24% | 75.47% |
| Recall | 88.57% | 91.43% |
| F1-score | 81.36% | 82.69% |

Feature selection produced the highest observed test F1-score among the experiments performed, increasing it from 0.8136 to 0.8269 while reducing the feature count.

## Final Observations

- Manual Linear Regression reproduced the Scikit-learn solution.
- Manual Logistic Regression provided a useful demonstration of gradient descent and binary classification.
- Increasing the learning rate improved training optimization but did not improve the fixed test-set metrics.
- The WIP missingness indicator did not improve the observed test performance.
- Feature selection improved the observed classification metrics while reducing dimensionality.

The feature-selected manual Logistic Regression model was the best-performing candidate among the configurations evaluated in the notebook.

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
202618064_LAB_005/
├── 202618064_lab5.ipynb
├── garments_worker_productivity.csv
├── outputs/
├── requirements.txt
├── .gitignore
└── README.md
```

## Conclusion

This lab demonstrates the complete workflow of a machine-learning experiment, from exploratory analysis and preprocessing to model implementation and optimization. Implementing regression and classification manually with NumPy provides insight into the underlying mathematics, while the experiments show how feature selection and preprocessing decisions can influence model performance.

Feature selection produced the highest observed test F1-score in the classification experiments, illustrating the value of evaluating alternative feature representations rather than relying exclusively on the initial model.
