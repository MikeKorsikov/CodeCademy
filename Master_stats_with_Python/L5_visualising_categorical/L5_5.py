import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# load in the data
df = pd.read_csv("Codecademy\Master_stats_with_Python\L5_visualising_categorical\mushroom_data.csv")
print(df.head())

# list of all column headers
columns = df.columns.tolist()

# 1
answer = "categorical and boolian"

# 2-5
for column in columns:
  print(column)
  sns.countplot(df[column], order=df[column].value_counts().index)

  #5
  plt.show()
  plt.clf()

  #6
  # rotates the value labels
  plt.xticks(rotation=30, fontsize=10)
  # increases font size 
  plt.xlabel(column, fontsize=12)

  #7
  plt.title(column + " Value Counts")