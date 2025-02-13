

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


student = pd.read_csv('c:/Users/nikol/Documents/PYTHON/Codecademy/Master_stats_with_Python/L9_linear_regression/student.csv')

# Convert non-numeric columns to numeric or drop them
student_numeric = student.select_dtypes(include=['number'])

# Save correlations here:
corrs = student_numeric.corr()

# Plot heatmap here:
sns.heatmap(corrs, xticklabels=corrs.columns, yticklabels=corrs.columns, vmin=-1, center=0, vmax=1, cmap='PuOr', annot=True)
plt.show()


