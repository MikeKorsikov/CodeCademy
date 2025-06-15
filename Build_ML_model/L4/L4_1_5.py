# Classify using sklearn

from movies import movie_dataset, labels
from sklearn.neighbors import KNeighborsClassifier

# 1 Create KNN
classifier = KNeighborsClassifier(n_neighbors = 5)

# 2 Train classifier 
classifier.fit(movie_dataset, labels)

# 3
points = [[.45, .2, .5], [.25, .8, .9], [.1, .1, .9]]

guesses = classifier.predict(points)
print(guesses)