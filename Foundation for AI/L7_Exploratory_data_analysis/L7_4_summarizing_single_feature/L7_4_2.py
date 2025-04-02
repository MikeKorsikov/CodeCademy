import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

movies = pd.read_csv('movies.csv')

# Create a boxplot for movie budget 
sns.boxplot(x='production_budget', data=movies)
plt.show()
plt.close()

# Create a histogram for movie budget
sns.histplot(x='production_budget', data=movies)
plt.show()
plt.close()

###

# Save the counts to genre_counts
genre_counts = movies.genre.value_counts()
print(genre_counts)

# Save the proportions to genre_props

genre_props = movies.genre.value_counts() / len(movies.genre)
print(genre_props)

###

# Create a bar chart for movie genre 
sns.countplot(x='genre', data=movies)
plt.show()
plt.close()


# Create a pie chart for movie genre
movies.genre.value_counts().plot.pie()
plt.show()
plt.close()
