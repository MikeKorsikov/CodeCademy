# project
import numpy as np
import pandas as pd
from scipy.stats import pearsonr, chi2_contingency
import matplotlib.pyplot as plt
import seaborn as sns

np.set_printoptions(suppress=True, precision = 2)

nba = pd.read_csv('Codecademy\Master_stats_with_Python\L6_variables_associations\games.csv')

# Subset Data to 2010 Season, 2014 Season
nba_2010 = nba[nba.year_id == 2010]
nba_2014 = nba[nba.year_id == 2014]

print(nba_2010.head())
print(nba_2014.head())

# 1 filter out teams and points
knicks_pts_10 = nba_2010["pts"][nba["fran_id"] == "Knicks"]
nets_pts_10 = nba_2010["pts"][nba["fran_id"] == "Nets"]

# 2 calculate means and difference of means
k_mean = np.mean(knicks_pts_10)
n_mean = np.mean(nets_pts_10)
diff_means_2010 = k_mean - n_mean
print(diff_means_2010)

# 3
plt.hist(knicks_pts_10, alpha=0.5, density = True, label='Knicks')
plt.hist(nets_pts_10, alpha=0.5, density = True, label='Nets')
plt.legend()
plt.title("NBA 2010 - Knicks & Nets")
plt.show()

# 4
knicks_pts_14 = nba_2014["pts"][nba["fran_id"] == "Knicks"]
nets_pts_14 = nba_2014["pts"][nba["fran_id"] == "Nets"]
k_mean = np.mean(knicks_pts_14)
n_mean = np.mean(nets_pts_14)
diff_means_2014 = k_mean - n_mean
print(diff_means_2014)

plt.clf()
plt.hist(knicks_pts_14, alpha=0.5, density = True, label='Knicks')
plt.hist(nets_pts_14, alpha=0.5, density = True, label='Nets')
plt.legend()
plt.title("NBA 2014 - Knicks & Nets")
plt.show()

# 5


# 6

# 7

# 8

# 9

# 10

# 11