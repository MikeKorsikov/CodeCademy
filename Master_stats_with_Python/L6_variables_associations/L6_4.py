# project on assoiations (covariance, correlation)
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
plt.clf()
sns.boxplot(data = nba_2010, x = "fran_id", y = "pts")
plt.show()

# 6
location_result_freq = pd.crosstab(nba_2010["game_result"], nba_2010["game_location"])
print(f"\nTable of frequencies: \n {location_result_freq}")

# 7
location_result_proportions = location_result_freq / len(nba_2010)
print(f"\nTable of proportions: \n {location_result_proportions}")

# 8
chi2, p, dof, expected = chi2_contingency(location_result_freq)
print(f"\nChi-Square statistic value: {chi2}")
print(f"\nExpected value table: \n {expected}")

# 9 Option 2 with numpy
point_diff_forecast_cov = np.cov(nba_2010['forecast'], nba_2010['point_diff'])
print(f"Covariance matrix between forecast and point_diff: \n {point_diff_forecast_cov}")
print(f"\nCovariance: {round(point_diff_forecast_cov[0,1],2)}")

# Option 2 with pandas
# Calculate the covariance matrix
point_diff_forecast_cov_matrix = nba_2010[["forecast", "point_diff"]].cov()

# Extract the covariance value between 'forecast' and 'point_diff'
point_diff_forecast_cov = point_diff_forecast_cov_matrix.loc["forecast", "point_diff"]

# Print the covariance value
print(f"\nCovariance between forecast and point_diff: {round(point_diff_forecast_cov,2)}")

# 10 Option 1 with scipy
point_diff_forecast_corr, p = pearsonr(nba_2010.forecast , nba_2010.point_diff)
print(f"Correlation (using SciPy): {round(point_diff_forecast_corr,2)}")

# Option 2 with Numpy
point_diff_forecast_corr = np.corrcoef(nba_2010['forecast'], nba_2010['point_diff'])[0, 1]
print(f"Correlation (using NumPy): {round(point_diff_forecast_corr,2)}")

#Option 3 with Pandas
point_diff_forecast_corr = nba_2010['forecast'].corr(nba_2010['point_diff'])
print(f"Correlation (using Pandas): {round(point_diff_forecast_corr,2)}")


# 11 Option 1 using seaborn
plt.clf()
sns.scatterplot(x=nba_2010['forecast'], y=nba_2010['point_diff'], alpha=0.5)
plt.xlabel("Win Probability (forecast)")
plt.ylabel("Point Differential (point_diff)")
plt.title("Scatter Plot of Forecast vs. Point Differential (NBA 2010)")
plt.axhline(0, color='red', linestyle='--', alpha=0.7)  # Reference line at y=0
plt.show()

# Option 2 using Matplotlib
plt.clf() #to clear the previous plot
plt.scatter('forecast', 'point_diff', data=nba_2010)
plt.xlabel('Forecasted Win Prob.')
plt.ylabel('Point Differential')
plt.show()