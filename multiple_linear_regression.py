# -*- coding: utf-8 -*-
"""multiple_linear_regression.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cDm5N1s6Pw3FO7x_wBIfw95Q7BQ_zoYA

# Multiple Linear Regression

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the dataset"""

dataset = pd.read_csv('Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

dataset.head()

dataset.describe()

print(X)

"""## Encoding categorical data"""

from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [3])], remainder='passthrough')
X = np.array(ct.fit_transform(X))

print(X)

"""## Splitting the dataset into the Training set and Test set"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

"""## Training the Multiple Linear Regression model on the Training set"""

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)

"""

```
# This is formatted as code
```

## Predicting the Test set results"""

y_pred = model.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

"""
Evaluating the Model

"""

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

"""
Creating the  Ridge Regression Model (L2 Regularization)\
"""

# Ridge Regression (L2 regularization)
from sklearn.linear_model import Ridge
ridge_model = Ridge(alpha=0.1)  # Adjust alpha for regularization strength
ridge_model.fit(X_train, y_train)

"""

Predicting the Ridge Regression Model(L2 Regularization)

"""

y_pred_ridge = ridge_model.predict(X_test)
print (y_pred_ridge)

"""

Evaluating the Ridge Regression Model (L2 Regularization)"""

mse_ridge = mean_squared_error(y_test, y_pred_ridge)
r2_ridge = r2_score(y_test, y_pred_ridge)


print("Ridge Regression:")
print("Mean Squared Error:", mse_ridge)
print("R-squared:", r2_ridge)

"""

Creating the Lasso Regression Model (L1 Regularization)
"""

from sklearn.linear_model import Lasso

lasso_model = Lasso(alpha=0.1)
lasso_model.fit(X_train, y_train)

"""
Predicting the Lasso Regression Model(L1 Regularization)
"""

y_pred_lasso = lasso_model.predict(X_test)
print(y_pred_lasso)

"""

Evaluate the Lasso Regression Model (L1 Regularization)
"""

mse_lasso = mean_squared_error(y_test, y_pred_lasso)
r2_lasso = r2_score(y_test, y_pred_lasso)


print("\nLasso Regression:")
print("Mean Squared Error:", mse_lasso)
print("R-squared:", r2_lasso)

"""
Creating the Model with Elastic Net

Elastic Net Regression combines L1 and L2 Regularization
"""

from sklearn.linear_model import ElasticNet
elastic_net_model = ElasticNet(alpha=0.1, l1_ratio=0.5)
elastic_net_model.fit(X_train, y_train)

"""
Predicting Elastic Net Regression
"""

y_pred_elastic_net = elastic_net_model.predict(X_test)

"""

Evaluating the Model"""

mse_elastic_net = mean_squared_error(y_test, y_pred_elastic_net)
r2_elastic_net = r2_score(y_test, y_pred_elastic_net)

print("Elastic Net Regression:")
print("Mean Squared Error:", mse_elastic_net)
print("R-squared:", r2_elastic_net)

"""
Visualizing and Comparing All Models
"""

import matplotlib.pyplot as plt

# Data for plotting
models = ['Linear Regression', 'Ridge Regression', 'Lasso Regression', 'Elastic Net']
mse_values = [mse, mse_ridge, mse_lasso, mse_elastic_net]
r2_values = [r2, r2_ridge, r2_lasso, r2_elastic_net]

# Create bar plots for MSE and R-squared
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.bar(models, mse_values)
plt.xlabel('Model')
plt.ylabel('Mean Squared Error')
plt.title('Mean Squared Error Comparison')

plt.subplot(1, 2, 2)
plt.bar(models, r2_values)
plt.xlabel('Model')
plt.ylabel('R-squared')
plt.title('R-squared Comparison')

plt.tight_layout()
plt.show()

"""
Evaluating the Intercept and Coefficient Values of All models
"""

import matplotlib.pyplot as plt



# Model names
models = ['Linear Regression', 'Ridge Regression', 'Lasso Regression', 'Elastic Net']


# Coefficients for Linear Regression
linear_coefficients = model.coef_

# Coefficients for Ridge Regression
ridge_coefficients = ridge_model.coef_

# Coefficients for Lasso Regression
lasso_coefficients = lasso_model.coef_

# Coefficients for Elastic Net Regression
elastic_net_coefficients = elastic_net_model.coef_


print("Linear Regression Coefficients:", linear_coefficients)
print("Ridge Regression Coefficients:", ridge_coefficients)
print("Lasso Regression Coefficients:", lasso_coefficients)
print("Elastic Net Regression Coefficients:", elastic_net_coefficients)


# Get intercepts
intercept_linear = model.intercept_
intercept_ridge = ridge_model.intercept_
intercept_lasso = lasso_model.intercept_
intercept_elastic_net = elastic_net_model.intercept_

print("Linear Regression Intercept:", intercept_linear)
print("Ridge Regression Intercept:", intercept_ridge)
print("Lasso Regression Intercept:", intercept_lasso)
print("Elastic Net Regression Intercept:", intercept_elastic_net)

# Intercept values
intercepts = [intercept_linear, intercept_ridge, intercept_lasso, intercept_elastic_net]

# Coefficients (assuming a 2D array)
coefficients = [
    linear_coefficients,
    ridge_coefficients,
    lasso_coefficients,
    elastic_net_coefficients
]

# Create subplots
fig, axs = plt.subplots(2, 2, figsize=(12, 8))

# Plot intercepts
axs[0, 0].bar(models, intercepts)
axs[0, 0].set_title('Intercept Comparison')
axs[0, 0].set_ylabel('Intercept Value')

# Plot coefficients (assuming you have only two features)
for i, coeffs in enumerate(coefficients):
    axs[1, 0].plot(range(len(coeffs)), coeffs, label=models[i])
axs[1, 0].set_title('Coefficient Comparison (Feature 1)')
axs[1, 0].set_xlabel('Feature')
axs[1, 0].set_ylabel('Coefficient Value')
axs[1, 0].legend()

# Plot coefficients for the second feature (if you have more features)
# ...

plt.tight_layout()
plt.show()

"""Final Verdict"""

print("Linear Regression")
print("Mean Squared Error:", mse)
print("R-squared:", r2)


print("Ridge Regression")
print("Mean Squared Error:", mse_ridge)
print("R-squared:", r2_ridge)


print("Lasso Regression")
print("Mean Squared Error:", mse_lasso)
print("R-squared:", r2_lasso)

print("Elasic Net Regression")
print("Mean Squared Error:", mse_elastic_net)
print("R-squared:", r2_elastic_net)

print("Almost all Models are around the same Mean squared, Elastic Net is little better than the other since it combines  L1 and L2 Regularization")