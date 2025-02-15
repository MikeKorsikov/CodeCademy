import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import numpy as np
import codecademylib3

hp = pd.read_csv('hp.csv')

print(hp.head())
print(hp.describe())

# Try a scatter plot of two quantitative variables
sns.lmplot(x='reviews', y='follows', fit_reg=False, data=hp)
plt.xlabel("Number of Words")
plt.ylabel("Number of Reviews")
plt.title("Scatter Plot of Words vs. Reviews")
plt.show()
plt.clf()

# Try the same plot colored by a binary variable
sns.lmplot(x='reviews', y='follows', hue='harry', markers=['o','x'], fit_reg=False, data=hp)
plt.xlabel("Number of Words")
plt.ylabel("Number of Reviews")
plt.title("Scatter Plot of Words vs. Reviews")
plt.show()
plt.clf()

# Try a model predicting a quantitative variable from two predictors
model0 = sm.OLS.from_formula('follows ~ reviews + harry', data=hp).fit()
print(model0.params)

# Try the same model but with an interaction term
model1 = sm.OLS.from_formula('follows ~ reviews + harry + reviews:harry', data=hp).fit()
print(model1.params)

# Try a polynomial model
model2 = sm.OLS.from_formula('follows ~ reviews + np.power(reviews, 3)', data=hp).fit()
print(model2.params)
