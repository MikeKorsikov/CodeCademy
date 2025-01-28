# pie charts

import matplotlib.pyplot as plt
import pandas as pd

water_usage = pd.read_csv("Codecademy\Master_stats_with_Python\L5_visualising_categorical\water_usage.csv")
print(water_usage.head())

wedge_sizes = water_usage['prop']
pie_labels = water_usage['water_source']

plt.pie(wedge_sizes, labels = pie_labels)
plt.axis('equal')
plt.title('Distribution of House Water Usage')
plt.show()
