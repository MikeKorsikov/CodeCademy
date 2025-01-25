# project 

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv("Codecademy/Master_stats_with_Python/L3_visualising/country_data.csv")

# 1: Inspect the dataset
print(data.head())
print(data.info())

# Convert columns to numeric and handle invalid entries
data["Life Expectancy"] = pd.to_numeric(data["Life Expectancy"], errors='coerce')
data["GDP"] = pd.to_numeric(data["GDP"], errors='coerce')

# Drop rows with missing values in key columns
data = data.dropna(subset=["Life Expectancy", "GDP"])

# 2: Extract life expectancy
life_expectancy = data["Life Expectancy"]

# 3: Calculate life expectancy quartiles
life_expectancy_quartiles = np.quantile(life_expectancy, [0.25, 0.5, 0.75])
print(f"Life Expectancy Quartiles: {life_expectancy_quartiles}")

# 4: Plot histogram of life expectancy
plt.hist(life_expectancy, bins=10, edgecolor="k")
plt.title("Life Expectancy Distribution")
plt.xlabel("Life Expectancy")
plt.ylabel("Frequency")
plt.show()

# 5: Answer variable
answer = 2

# 6: Extract GDP
gdp = data["GDP"]

# 7: Calculate median GDP
median_gdp = float(np.median(gdp))
print(f"Median GDP: {median_gdp}")
print(f"Type of median_gdp: {type(median_gdp)}")

# 8: Split data into low and high GDP groups
low_gdp = data[data["GDP"] <= median_gdp]
high_gdp = data[data["GDP"] > median_gdp]
#print(low_gdp.head())
#print(high_gdp.head())

# 9: Calculate quartiles for life expectancy in low GDP countries
low_gdp_life_expectancy = low_gdp["Life Expectancy"]
low_gdp_quartiles = np.quantile(low_gdp_life_expectancy, [0.25, 0.5, 0.75])
print(f"Low GDP Life Expectancy Quartiles: {low_gdp_quartiles}")

# 10
high_gdp_life_expectancy = high_gdp["Life Expectancy"]
high_gdp_quartiles = np.quantile(high_gdp_life_expectancy, [0.25, 0.5, 0.75])
print(f"High GDP Life Expectancy Quartiles: {high_gdp_quartiles}")

# 11
plt.hist(high_gdp["Life Expectancy"], alpha = 0.5, label = "High GDP")
plt.hist(low_gdp["Life Expectancy"], alpha = 0.5, label = "Low GDP")
plt.legend()
plt.show()