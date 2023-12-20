# Breast Cancer Prediction Model

This project aims to predict breast cancer using various machine learning algorithms. The dataset used for this project contains several features, including mean radius, mean texture, mean perimeter, mean area, mean smoothness, mean compactness, mean concavity, mean concave points, mean symmetry, and mean fractal dimension.

## Project Overview

The project follows the subsequent steps:

1. Data Preprocessing: The dataset is cleaned, missing values are handled, and necessary preprocessing steps are performed.

2. Exploratory Data Analysis (EDA): Data visualization techniques are employed to gain insights into the dataset and understand the relationships between different features.

3. Model Building: Several machine learning models are trained and evaluated to predict breast cancer. The models used include Logistic Regression, Decision Tree Classifier, Random Forest Classifier, Naive Bayes, and K-Nearest Neighbors Classifier.

4. Model Evaluation: The models' performances are evaluated using various metrics such as accuracy score, confusion matrix, and F1 score.

5. Model Optimization: Grid Search algorithm is implemented to tune the hyperparameters of the models and improve their performance.

6. Model Export: The best-performing model is exported using the pickle library for deployment.

## Repository Structure

The repository includes the following files:

- `data.csv`: The dataset containing information about breast cancer patients.
- `model.pkl`: The serialized machine learning model, ready for deployment.
- `boobs.ipynb`: Jupyter Notebook containing the Python code used for data preprocessing, EDA, model building, and optimization.

## Requirements

The following Python libraries are required to run the code:

- `numpy`
- `pandas`
- `seaborn`
- `plotly`
- `matplotlib`
- `scikit-learn`

Ensure that these libraries are installed before running the code.

## How to Run the Code

To run the code:

1. Clone the repository to your local machine.
2. Install the necessary Python libraries mentioned in the `Requirements` section.
3. Run the Jupyter Notebook `prediction.ipynb` to execute the code step-by-step.
4. Run python3 app.py in your terminal to see the deployed model

## Results

The project achieves an accuracy of 91.8% and effectively predicts breast cancer with the deployed model.

## Acknowledgments

The dataset used in this project is publicly available and can be accessed at https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset

