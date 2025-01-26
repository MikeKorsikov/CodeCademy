# project
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

healthcare = pd.read_csv("Codecademy\Master_stats_with_Python\L3_visualising\healthcare.csv")

# 1
#print(healthcare.head())
print(healthcare.info())

# 2
#print(healthcare["DRG Definition"].unique())

# 3 
chest_pain = healthcare[healthcare['DRG Definition'] == '313 - CHEST PAIN']
print(chest_pain.head())

# 4
alabama_chest_pain = chest_pain[chest_pain['Provider State'] == "AL"]
print(alabama_chest_pain.head())

# 5
costs = alabama_chest_pain[' Average Covered Charges '].values
costs_mean= round(np.mean(costs),0)
costs_median = round(np.median(costs),0)
print(f"Mean: {costs_mean}")
print(f"Median: {costs_median}")

# 6 Chest pain costs in Alabama hospitals
#plt.boxplot(costs)
#plt.show()

# 7
states = sorted(chest_pain["Provider State"].unique())
print(states)

# 8
datasets = []
for state in states:
  datasets.append(chest_pain[chest_pain['Provider State'] == state][' Average Covered Charges '].values)

# 9
plt.figure(figsize=(20,6))

# 10
plt.boxplot(datasets, labels=states)
plt.show()