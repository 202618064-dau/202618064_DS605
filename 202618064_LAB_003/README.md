# DS605 Lab 3 - Scikit-learn Preprocessing and Model Evaluation

## Student Details

**Name:** Gauri Dawar  
**ID:** 202618064  
**Course:** MSc Data Science  
**Subject:** DS605 - Fundamentals of Machine Learning

---

## Objective

The aim of this lab is to preprocess the Hotel Booking Demand dataset using
Scikit-learn and compare Logistic Regression and Decision Tree models using
different preprocessing pipelines.

## Dataset

Dataset: Hotel Booking Demand

Source: Kaggle - Hotel Booking Demand Dataset

The dataset used in this lab is `hotel_bookings.csv`.

---

## Tasks Covered

### Task 1 - Data Loading and Understanding
- Loaded and explored the dataset.
- Checked the shape, data types and basic statistics.
- Checked the distribution of `is_canceled`.
- Used `is_canceled` as the target variable.
- Separated numerical and categorical features.

### Task 2 - Missing Values, Leakage and Outliers
- Checked missing values in the dataset.
- Removed columns that could reveal the booking outcome:
  `reservation_status` and `reservation_status_date`.
- Checked selected numerical features using boxplots and IQR.
- Removed only the extreme outliers considered unsuitable for modelling.

### Task 3 - Preprocessing Pipelines

Two preprocessing pipelines were created.

**Pipeline A**
- KNNImputer
- StandardScaler

**Pipeline B**
- KNNImputer
- MinMaxScaler

For categorical columns:
- SimpleImputer with `most_frequent`
- OneHotEncoder with `handle_unknown="ignore"`

ColumnTransformer was used to apply different preprocessing methods to
numerical and categorical columns.

### Task 4 - Classification Models

Two classification models were trained:

1. Logistic Regression
2. Decision Tree Classifier

The same train-test split was used for all four experiments.

### Task 5 - Model Evaluation

The models were compared using:

- Training Accuracy
- Testing Accuracy
- Precision
- Recall
- F1-score

Confusion matrices were also created for the best Logistic Regression
and Decision Tree results.

---

## Final Results

Overall, Decision Tree with StandardScaler performed the best. Scaling made a small difference to Logistic Regression but almost no difference to Decision Tree. The Decision Tree also shows some overfitting because its training accuracy is much higher than its test accuracy.

## Final Observations

1. Decision Tree with Pipeline A gave the best overall result with a test
   accuracy of 85.63% and F1-score of 0.8185.

2. Logistic Regression performed slightly better with StandardScaler than
   with MinMaxScaler.

3. Scaling had almost no effect on the Decision Tree because its results
   with both pipelines were nearly the same.

4. The Decision Tree correctly classified more cancelled and non-cancelled
   bookings according to the confusion matrix.

5. The Decision Tree has a high training accuracy compared to its test
   accuracy, which indicates some overfitting.

## Conclusion

Overall, the Decision Tree with Pipeline A performed best among the four
experiments. StandardScaler was slightly more useful for Logistic Regression,
while changing the scaler made almost no difference to the Decision Tree.