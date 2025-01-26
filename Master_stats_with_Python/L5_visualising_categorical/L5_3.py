import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Codecademy\Master_stats_with_Python\L5_visualising_categorical\school_data.csv")
print(df.head())

value_order = ["NOT ENOUGH DATA", "VERY WEAK", "WEAK", "NEUTRAL", "STRONG", "VERY STRONG"]

type_of_data = "ordinal"


# plot using .countplot() method here
sns.countplot(df["Supportive Environment"], order=value_order)

plt.xticks(rotation=30)

# show your plot here
plt.show()