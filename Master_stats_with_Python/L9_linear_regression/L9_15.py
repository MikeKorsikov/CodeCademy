import pandas as pd
import statsmodels.api as sm
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
family = pd.read_csv('Codecademy\Master_stats_with_Python\L9_linear_regression\\family.csv')

#create heat map here:
print("\nExercise 1:")
corr_grid = family.select_dtypes(include=['number']).corr()
sns.heatmap(corr_grid, xticklabels=corr_grid.columns, yticklabels=corr_grid.columns, vmin=-1, center=0, vmax=1, cmap='PuOr', annot=True)
plt.title("Heat Map of Correlations")
plt.show()

#fit model and view summary here:
print("\nExercise 2:")
model = sm.OLS.from_formula('income ~ food + housing + source', family)
results = model.fit()
print(results.summary())

#write out regression equation here:
print("\nExercise 3:")
print(results.params)
# income = -26.8 + 29.7 * source + 1.52 * food + 3.18 * housing

#interpret intercept here:
print("\nExercise 4:")
print("When food and housing expenditures are zero pesos, the average income is -26.8")

#interpret the coefficient on source here:
print("\nExercise 5:")
print("All other variables constant, the average income is 29.7")

#interpret the coefficient on food here:
print("\nExercise 6:")
print("All other predictors constant, as food expenditure increases by 1, expected income increases by about 1.5")

#interpret the coefficient on housing here:
print("\nExercise 7:")
print("All other predictors constant, as as housing expenditure increases by 1, expected income increases by about 3.2")

#plot regression lines on scatter plot here:
print("\nExercise 8:")

sns.lmplot(x='housing', y='income', hue='source', data=family)
plt.plot(family.housing, results.params[0]+results.params[1]*1+results.params[3]*family.housing+results.params[2]*10, color='red',linewidth=5, label='food=10')
plt.plot(family.housing, results.params[0]+results.params[1]*1+results.params[3]*family.housing+results.params[2]*100, color='orange',linewidth=5, label='food=100')
plt.plot(family.housing, results.params[0]+results.params[1]*1+results.params[3]*family.housing+results.params[2]*200, color='yellow',linewidth=5, label='food=200')
plt.legend()
plt.show()