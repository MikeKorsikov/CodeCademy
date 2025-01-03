import pandas as pd
import numpy as np

# Get NYC Trees Data
nyc_trees = pd.read_csv('nyc_tree_census.csv')
print(nyc_trees.info())

#
living_frequency = np.sum(nyc_trees['status'] == 'Alive')
print(f"Frequency: {living_frequency}")

living_proportion = (nyc_trees['status'] == 'Alive').mean()
print(f"Proportion: {living_proportion}")

#
print(nyc_trees['trunk_diam'])

giant_frequency  = np.sum(nyc_trees['trunk_diam'] > 30)
print(f"Frequency: {giant_frequency}")

giant_proportion  = (nyc_trees['trunk_diam'] > 30).mean()
print(f"Proportion: {giant_proportion}")