# DS605 Lab 8: Decision Tree and SVM from Scratch

**Name: Gauri Dawar**

**ID: 202618064**

## Overview
This lab implements a Decision Tree and a Linear Support Vector Machine (SVM) from scratch and compares their performance with Scikit-learn implementations. It also explores nonlinear SVM kernels using a synthetic dataset.

## Dataset
**Banknote Authentication Dataset**
- Samples: 1,372
- Features: 4 — variance, skewness, curtosis, entropy
- Target: 2 classes (0 and 1)

A `make_moons` dataset is also used to compare nonlinear SVM kernels.

## Implementation

### Part A: Decision Tree from Scratch
- Implemented Gini impurity and Entropy.
- Implemented best-split selection and recursive tree construction.
- Implemented prediction and evaluation.
- Visualized the tree structure and decision boundaries.
- Compared Gini and Entropy and explored maximum tree depth.
- Compared the manual tree with Scikit-learn's Decision Tree.

### Part B: Linear SVM from Scratch
- Standardized the input features and converted labels to -1 and +1.
- Implemented hinge loss, gradients, and gradient descent.
- Evaluated classification performance.
- Visualized the decision boundary, margins, and margin-violating samples.
- Experimented with different values of C.
- Compared the manual SVM with Scikit-learn's Linear SVM.

### Part C: Nonlinear SVM
- Generated a `make_moons` dataset.
- Compared Linear, Polynomial, and RBF kernels.
- Visualized their decision boundaries and compared performance.

### Part D: Final Model Comparison
Compared five models using accuracy, precision, recall, F1-score, training time, and prediction time:
- Manual Decision Tree
- Scikit-learn Decision Tree
- Manual Linear SVM
- Scikit-learn Linear SVM
- RBF SVM

## Results

| Model | Test Accuracy |
|---|---:|
| Manual Decision Tree | 99.27% |
| Scikit-learn Decision Tree | 99.27% |
| Manual Linear SVM (C = 10) | 97.09% |
| Scikit-learn Linear SVM | 100% |
| RBF SVM | 100% |

On the `make_moons` dataset, the RBF SVM achieved 99% accuracy.

## Conclusion
The Decision Trees achieved 99.27% accuracy, while the Scikit-learn Linear SVM and RBF SVM achieved 100% on the banknote test set. The experiments demonstrate the importance of model selection, feature scaling, hyperparameter tuning, and nonlinear kernels.

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
