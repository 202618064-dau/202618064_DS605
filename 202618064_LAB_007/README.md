# DS605 Lab 7: Image Representation, PCA and Face Recognition

**Student ID:** 202618064

## Overview

This project implements image representation, Principal Component Analysis (PCA), eigenfaces, image reconstruction and face recognition using the AT&T Database of Faces (ORL).

PCA is implemented using NumPy linear-algebra operations rather than Scikit-learn's PCA implementation, as required by the assignment.

## Dataset

The ORL dataset contains 400 grayscale face images from 40 subjects, with 10 images per subject.

Download the dataset from the [AT&T Database of Faces website](https://cam-orl.co.uk/facedatabase.html).

Extract the dataset into an `att_faces/` directory inside the project folder. The dataset is excluded from this repository.

## Implementation

### Part A: Image Representation
- Load grayscale images and inspect pixel dimensions and intensity values.
- Flatten images into numerical feature vectors.
- Create subject labels and a reproducible train-test split.
- Use 280 images for training and 120 for testing.

### Part B: PCA, Eigenfaces and Compression
- Calculate the mean face and center the training data.
- Implement PCA using covariance eigendecomposition and SVD with NumPy.
- Plot cumulative explained variance and visualize eigenfaces.
- Project images into PCA space and reconstruct test images.
- Compare reconstruction error and numerical storage requirements.

### Part C: Face Recognition
- Match test images with the closest training images using Euclidean distance.
- Compare raw-pixel and PCA-space recognition.
- Inspect correct and incorrect predictions.

### Part D: Traditional Machine Learning
- Train KNN, SVM and Logistic Regression classifiers using PCA features.
- Compare recognition performance at different explained-variance thresholds.
- Tune model hyperparameters using stratified cross-validation.

## Initial Results

| Method | Accuracy |
|---|---:|
| Raw-pixel nearest face | 97.50% |
| PCA nearest face | 97.50% |
| PCA + KNN (k=3) | 93.33% |
| PCA + SVM (RBF) | 98.33% |
| PCA + Logistic Regression | 99.17% |

The best observed tuned configuration was **Logistic Regression with 28 PCA components** and `C=1`, achieving 97.50% mean cross-validation accuracy and 99.17% test accuracy.

These results apply to the current train-test split and tested configurations.

## Project Structure

```text
202618064_LAB_007/
├── att_faces/                     # Local dataset, excluded from Git
├── outputs/
├── 202618064_lab7.ipynb
├── requirements.txt
├── .gitignore
└── README.md
```

## Requirements

- Python 3.11
- NumPy
- Matplotlib
- Pillow
- Scikit-learn
- Pandas
- Jupyter

Install the dependencies with:

```bash
python -m pip install -r requirements.txt
```

Open `202618064_lab7.ipynb` in VS Code and run the cells from top to bottom after downloading and extracting the dataset.

## Conclusion

This assignment demonstrates how PCA can reduce image dimensionality while retaining useful information for face recognition. The experiments compare similarity-based matching with traditional classifiers and examine the effects of component selection and hyperparameter tuning.
