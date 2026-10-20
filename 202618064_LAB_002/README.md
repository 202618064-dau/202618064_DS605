# DS605 Lab 2: NumPy Vectorization and Pandas Data Wrangling

## Overview

This lab focuses on numerical computing with **NumPy** and data manipulation, analysis, and visualization with **Pandas**. The first part explores array operations, statistical calculations, and linear algebra. The second part applies data-wrangling techniques to the Titanic dataset to investigate passenger survival patterns.

The lab emphasizes practical implementation, exploratory data analysis (EDA), missing-value handling, outlier detection, feature engineering, aggregation, and visualization.

## Objectives

- Create and manipulate NumPy arrays of different dimensions.
- Perform vectorized arithmetic and linear algebra operations.
- Generate normally distributed data and visualize it using histograms.
- Load, inspect, filter, and query tabular data using Pandas.
- Perform grouping, aggregation, and pivot-table analysis.
- Identify missing values and compare imputation techniques.
- Detect potential outliers using the Interquartile Range (IQR) method.
- Engineer new features from existing columns.
- Visualize relationships and investigate factors associated with passenger survival.

## Dataset

**Dataset:** Titanic Passenger Dataset  
**File:** `train.csv`

The dataset contains information about passengers aboard the Titanic, including:

- `Survived` — survival outcome (0 = did not survive, 1 = survived)
- `Pclass` — passenger class
- `Sex` — passenger sex
- `Age` — passenger age
- `SibSp` — number of siblings or spouses aboard
- `Parch` — number of parents or children aboard
- `Fare` — passenger fare
- `Embarked` — port of embarkation
- `Cabin`, `Name`, `Ticket`, and other passenger details

The notebook loads the dataset from `202618064_LAB_002/train.csv`.

The dataset contains **891 rows and 12 columns** before feature engineering.

## Part A — Vectorized Programming with NumPy

### Task 1: Arrays, Statistics, and Indexing

Created and manipulated NumPy arrays using different array-generation functions.

**Concepts covered:**
- Random integer generation using `np.random.randint()`
- Array creation using `np.arange()`, `np.zeros()`, `np.ones()`, and `np.linspace()`
- Statistical calculations: minimum, maximum, mean, median, and standard deviation
- Array dimensions, shape, indexing, and slicing
- Reshaping and flattening arrays using `reshape()` and `flatten()`
- Accessing elements in one-dimensional, two-dimensional, and three-dimensional arrays

### Task 2: Vectorized Arithmetic and Linear Algebra

Performed arithmetic and matrix operations using NumPy.

**Operations covered:**
- Element-wise matrix addition and multiplication
- Matrix multiplication using the `@` operator
- Matrix transpose using `.T`
- Determinant calculation using `np.linalg.det()`
- Matrix inverse using `np.linalg.inv()`
- Verification of the inverse using `np.allclose()`

These operations demonstrate how NumPy performs numerical calculations efficiently without requiring explicit Python loops for basic array arithmetic.

### Task 3: Normal Distribution and Histogram

Generated 10,000 random values from a normal distribution with:

- Mean (\(\mu\)) = 50
- Standard deviation (\(\sigma\)) = 10

Calculated the sample mean and sample standard deviation, then plotted a histogram to examine the distribution.

This task demonstrates random sampling, descriptive statistics, and basic statistical visualization.

## Part B — Data Wrangling with Pandas

### Task 4: Loading and Inspecting Data

Loaded the Titanic dataset and explored its structure using Pandas.

**Functions covered:**
- `head()` and `tail()`
- `shape` and `columns`
- `info()` and `describe()`
- `loc[]` for label-based selection
- `iloc[]` for position-based selection

The inspection identified missing values in columns such as `Age` and `Cabin`.

### Task 5: Filtering and Querying

Used Boolean indexing and compound conditions to answer questions about passenger demographics and survival.

Examples included:

- Identifying male passengers older than 50.
- Calculating the survival percentage of female first-class passengers.
- Finding survivors aged 20–40 who paid above the overall median fare.
- Identifying passengers travelling alone, younger than 30, who did not survive.
- Filtering passengers who embarked at Southampton, travelled in second or third class, and paid above the Southampton fare median.

This task demonstrates combining logical conditions, comparisons, and `isin()` to extract specific subsets of data.

### Task 6: Grouping and Aggregation

Used `groupby()` and aggregation functions to compare passenger statistics.

The analysis included:

- Survival rates by sex.
- Survival rates by passenger class.
- Average age and fare by passenger class.
- Passenger counts and survival rates for each sex-class combination.
- Passenger counts, average fares, and survival rates by embarkation port.

The results show noticeable differences in survival rates across passenger groups.

### Task 7: Missing Values and Fare Outliers

Investigated missing data and compared multiple approaches to imputing missing `Age` values.

**Imputation techniques:**
- Mean imputation
- Median imputation
- Mode imputation
- Random-value imputation using observed age values

Also calculated the first quartile (Q1), third quartile (Q3), and Interquartile Range (IQR) for `Fare`.

The outlier limits were calculated using:

\[
\text{Lower Bound}=Q_1-1.5\times IQR
\]

\[
\text{Upper Bound}=Q_3+1.5\times IQR
\]

Fare observations outside these limits were identified as potential outliers. This task focuses on detecting outliers rather than automatically removing them.

### Task 8: Feature Engineering and Pivot Tables

Created two additional features:

- **`FamilySize`** — total family size, calculated as `SibSp + Parch + 1`.
- **`IsAlone`** — a binary indicator equal to 1 when the passenger is travelling without family members and 0 otherwise.

A pivot table was then created to compare survival rates across combinations of sex and passenger class.

The highest and lowest survival-rate groups were identified from the resulting table.

### Task 9: Data Visualization and Observations

Created visualizations to explore relationships in the dataset.

**Visualizations included:**

- Correlation heatmap for selected numerical features.
- Bar chart of survival rates by sex.
- Scatter plot of age versus fare, distinguishing survivors from non-survivors.
- Pair plot of selected numerical variables, with observations grouped by survival status.

The visualizations helped identify patterns associated with passenger survival and relationships between numerical variables.

## Key Findings

The exploratory analysis produced the following observations:

- **Sex:** Female passengers had a considerably higher survival rate than male passengers.
- **Passenger class:** First-class passengers generally had higher survival rates than passengers in second and third class.
- **Sex and passenger class:** Survival rates varied noticeably across sex-class combinations.
- **Fare and passenger class:** These variables showed a strong relationship, as passengers in higher classes generally paid higher fares.
- **Age and fare:** Most passengers paid relatively lower fares, with a smaller number paying substantially higher fares.
- **Missing data:** Age contained missing values, while Cabin had a much larger amount of missing information.
- **Correlation analysis:** Relationships between numerical variables varied in strength; correlation alone does not establish causation.


## Project Structure

```text
202618064_LAB_002/
├── 202618064_LAB_002.ipynb
├── train.csv
└── README.md
```


## Conclusion

This lab establishes a foundation in numerical computing and data wrangling. NumPy was used for array manipulation, vectorized arithmetic, linear algebra, and statistical sampling. Pandas was used to inspect, filter, aggregate, and transform the Titanic dataset.

The analysis highlighted differences in survival rates by sex and passenger class, demonstrated methods for handling missing values, and introduced outlier detection, feature engineering, and visualization. These skills form an important foundation for subsequent exploratory data analysis and machine learning workflows.
