# FetchMaker

# Import libraries
import numpy as np
import pandas as pd


# Import data
dogs = pd.read_csv('Codecademy\Master_stats_with_Python\L8_hypothesis_testing\dog_data.csv')

# Subset to just whippets, terriers, and pitbulls
dogs_wtp = dogs[dogs.breed.isin(['whippet', 'terrier', 'pitbull'])]

# Subset to just poodles and shihtzus
dogs_ps = dogs[dogs.breed.isin(['poodle', 'shihtzu'])]