import pandas as pd
import numpy as np

car_eval = pd.read_csv('Codecademy\math_DS\summary_stats\car_eval_dataset.csv')
print(car_eval.head())
print(car_eval.info())


# 1
print("\n Exercise 1")
# Total frequency
manufacturer_country_counts = car_eval['manufacturer_country'].value_counts()
print(manufacturer_country_counts)

# Modal category
print(f"\nModal: {manufacturer_country_counts.index[0]}")

# 4th most frequent
print(f"\n4th most frequent: {manufacturer_country_counts.index[3]}")

# 2
print("\n Exercise 2")
# Proportion of countries
manufacturer_country_relative = car_eval['manufacturer_country'].value_counts(normalize=True)
print(manufacturer_country_relative)

# Japan's share
print(f"\nJapan's share: {manufacturer_country_relative[0]*100}%")

# 3
print("\n Exercise 3")
# possible categories buying_cost             
unique_values = car_eval['buying_cost'].unique()
print(f"\nPossible categories: {unique_values}")

# 4
print("\n Exercise 4")
buying_cost_categories = ["low", "med", "high", "vhigh"]

# 5 
print("\n Exercise 5")
# converting to category
car_eval.buying_cost = pd.Categorical(car_eval.buying_cost, buying_cost_categories, ordered=True)

# checking
print(car_eval.info())

# 6
print("\n Exercise 6")
median_buying_cost_index = np.median(car_eval["buying_cost"].cat.codes)
print(f"Median index: {median_buying_cost_index}")
print(f"Median category: {buying_cost_categories[int(median_buying_cost_index)]}")

# 7
print("\n Exercise 7")
luggage_relative = car_eval['luggage'].value_counts(normalize=True)
print(luggage_relative)

# 8
print("\n Exercise 8")
luggage_freq = car_eval['luggage'].value_counts()
print(luggage_freq) # there are no missing values
luggage__relative_gross = car_eval['luggage'].value_counts(dropna = False, normalize=True)
print(luggage__relative_gross)

# 9
print("\n Exercise 9")
luggage_freq_2 = luggage_freq / len(car_eval['luggage'])
print(luggage_freq_2)

# 10
print("\n Exercise 10")
unique_values_doors = car_eval['doors'].unique()
print(f"Categories: {unique_values_doors}")

cars_with_5_or_more = np.sum(car_eval['doors'] == "5more")
print(f"Numner of cars with 5+ doors: {cars_with_5_or_more}")

# 11
print("\n Exercise 11")
total_cars =  len(car_eval['doors'])
print(f"Total number of cars: {total_cars}")

cars_with_5_or_more_relative = cars_with_5_or_more / total_cars
print(f"Proportion of cars with 5 doors or more: {cars_with_5_or_more_relative*100}%")







