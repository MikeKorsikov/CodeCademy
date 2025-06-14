# Evaluating the Model's Accuracy
# Technique: Residual Analysis
# R² is the percentage variation in y explained by all the x variables together
# The best is 1.0, the worst is 0.0, good is >= 0.7

import matplotlib.pyplot as plt
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

streeteasy = pd.read_csv("https://raw.githubusercontent.com/sonnynomnom/Codecademy-Machine-Learning-Fundamentals/master/StreetEasy/brooklyn.csv")

df = pd.DataFrame(streeteasy)

x = df[['bedrooms', 'bathrooms', 'size_sqft', 'min_to_subway', 'floor', 'building_age_yrs', 'no_fee', 'has_roofdeck', 'has_washer_dryer', 'has_doorman', 'has_elevator', 'has_dishwasher', 'has_patio', 'has_gym']]
y = df[['rent']]

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size = 0.8, test_size = 0.2, random_state=6)

mlr = LinearRegression()

model=mlr.fit(x_train, y_train)

y_predict = mlr.predict(x_test)

# Print the coefficients of the model
print(mlr.coef_)

# we can add or remove features from the model to improve the accuracy

# Input code here:
print("\nTrain R² score:")
print(mlr.score(x_train, y_train))

print("\nTest R² score:")
print(mlr.score(x_test, y_test))

