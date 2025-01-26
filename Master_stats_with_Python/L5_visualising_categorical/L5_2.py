import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Codecademy\Master_stats_with_Python\L5_visualising_categorical\games.csv")
print(df.head())
print(df.info())

#
sns.countplot(df["victory_status"], 
              order=df["victory_status"].value_counts(ascending=True).index)

plt.show()