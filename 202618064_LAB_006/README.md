# DS605 Lab 6: Image Representation and Text Classification

**Name: Gauri Dawar**
**ID: 202618064**

## Overview

This lab explores feature extraction, feature representation, and traditional machine-learning classification through two tasks:

1. **Asphalt Crack Classification:** Classifying images as crack or non-crack using handcrafted image features.
2. **Email Spam Classification:** Classifying emails as spam or non-spam using text-based numerical features.

The experiments compare Logistic Regression and Random Forest, investigate improvements to feature representations, and evaluate the trade-off between classification performance and computational cost.

## Objectives

- Extract numerical features from images using OpenCV and NumPy.
- Apply grayscale conversion, resizing, intensity statistics, and Canny edge detection.
- Train and evaluate traditional machine-learning classifiers.
- Improve image representation by adjusting Canny edge-detection thresholds.
- Perform email spam classification using 3,000 text features.
- Apply Chi-square feature selection to reduce dimensionality.
- Compare accuracy, precision, recall, F1-score, and computational time.

## Part A: Asphalt Crack Classification

### Dataset

The asphalt image dataset is organized into two classes:

- `Cracks`
- `NonCracks`

The notebook uses the `448` directory as the dataset root. The images are resized to 128 × 128 pixels and converted to grayscale for feature extraction.

### Feature Extraction

Nine handcrafted features are extracted from each image:

- Mean brightness
- Contrast
- Additional intensity statistics
- Dark-pixel ratio
- Bright-pixel ratio
- Canny edge-based features

The extracted features form a numerical dataset that can be used by traditional machine-learning classifiers.

### Baseline Models

Two classifiers are evaluated:

| Model | Accuracy | F1-score |
|---|---:|---:|
| Logistic Regression | 93.75% | 93.83% |
| Random Forest | 95.00% | 95.00% |

Random Forest outperformed the baseline Logistic Regression model in test accuracy, while Logistic Regression had lower measured training and prediction times.

### Improved Image Representation

The Canny edge-detection thresholds were increased from `(100, 200)` to `(150, 250)` to obtain a more selective edge representation.

| Metric | Baseline Logistic Regression | Improved Logistic Regression |
|---|---:|---:|
| Accuracy | 93.75% | 95.00% |
| F1-score | 93.83% | 95.12% |
| Recall | 95.00% | 97.50% |
| Mean edge density | 0.2716 | 0.1909 |

The improved representation increased Logistic Regression accuracy by 1.25 percentage points and reduced the mean edge density. Random Forest maintained 95.00% accuracy with both representations.

**Best result for Part A:** Improved Logistic Regression, with 95.00% accuracy and 95.12% F1-score.

## Part B: Email Spam Classification

### Dataset

The notebook uses an email spam dataset containing 5,172 emails, represented by 3,000 numerical text features.

The dataset contains:

- 3,672 non-spam emails
- 1,500 spam emails

The data is split into training and testing sets, with 4,137 training samples and 1,035 test samples.

### Baseline Models

Logistic Regression and Random Forest are evaluated using the original 3,000 features.

| Model | Accuracy | F1-score |
|---|---:|---:|
| Logistic Regression | 98.26% | 97.04% |
| Random Forest | 96.43% | 93.86% |

Logistic Regression achieved the stronger baseline performance, correctly classifying 1,017 out of 1,035 test emails.

### Feature Selection with Chi-square

Chi-square feature selection was used to reduce the feature count from 3,000 to 1,000.

| Metric | Original Logistic Regression | Reduced Logistic Regression |
|---|---:|---:|
| Number of features | 3,000 | 1,000 |
| Accuracy | 98.26% | 97.29% |
| F1-score | 97.04% | 95.36% |
| Training time | 9.76 s | 4.49 s |
| Prediction time | 0.147 s | 0.010 s |

Feature selection reduced the number of features by 66.7%. It also reduced training and prediction time, with a modest decrease in classification performance.

**Best result for Part B:** Logistic Regression using the original 3,000 features, achieving 98.26% accuracy and 97.04% F1-score.

## Key Findings

- Handcrafted image features can support effective asphalt crack classification.
- Adjusting Canny thresholds improved Logistic Regression performance on the crack dataset.
- Logistic Regression outperformed Random Forest on the email spam dataset in the reported evaluation.
- Chi-square feature selection reduced dimensionality and computational cost, but slightly reduced classification performance.
- The experiments demonstrate that feature representation affects both predictive performance and computational efficiency.

## Technologies Used

- Python
- NumPy
- Pandas
- OpenCV
- Matplotlib
- Scikit-learn
- Jupyter Notebook

## Project Structure

```text
202618064_LAB_006/
├── 448/
│   ├── Cracks/
│   └── NonCracks/
├── 202618064_lab6.ipynb
├── outputs/
├── requirements.txt
├── .gitignore
└── README.md
```


## Conclusion

This lab demonstrates the importance of feature extraction and feature selection in traditional machine learning. The asphalt crack experiment showed that a more selective Canny representation improved Logistic Regression performance. The email spam experiment showed that Logistic Regression performed well with the original text features, while Chi-square selection reduced computational cost at the expense of some predictive performance.

Overall, the results illustrate the trade-off between feature dimensionality, classification quality, and computational efficiency.