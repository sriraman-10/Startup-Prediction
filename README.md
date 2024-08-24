Project Title: Startup Prediction

Description:
This project aims to predict the success of startups based on various factors using multiple linear regression techniques. The project utilizes a dataset containing information about startups, including their industry, funding, and growth metrics.

Dataset:

Name: Startup.csv
Description: Contains features such as industry, founding year, funding amount, and growth metrics for a set of startups.
Data Preprocessing:



Linear Regression: Baseline model for comparison.
Ridge Regression: Used to address overfitting by adding a regularization term. L2
Lasso Regression: Used for feature selection and regularization. L1
Elastic Net: Combines Ridge and Lasso for a balance of regularization and feature selection. L1 + L2
Evaluation Metrics:

Mean Squared Error (MSE): Measures the average squared difference between predicted and actual values.
R-squared (R²): Indicates the proportion of variance explained by the model.   
Results:

Model Comparison: Compare the performance of different models based on MSE and R-squared.
Feature Importance: Analyze the coefficients of the models to identify the most influential features.
Usage:

Clone the repository: git clone https://github.com/sriraman-10/Startup-Prediction.git
Run the Jupyter Notebook: jupyter notebook multiple_linear_regression.ipynb


