# X matrix
import pandas as pd
import patsy
import statsmodels.api as sm

#  fit a regression predicting rent based on borough
rentals = pd.read_csv('rentals.csv')
y, X = patsy.dmatrices('rent ~ borough', rentals)

# Print out the first 5 rows of X
print(X[0:5])

# fit a linear regression model
model = sm.OLS.from_formula('rent ~ borough', rentals).fit()
print(model.params)
