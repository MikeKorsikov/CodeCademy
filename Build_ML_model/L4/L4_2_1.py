# KNN regression is a type of algorithm used for regression tasks.

from movies import movie_dataset, movie_ratings

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def predict(unknown, dataset, movie_ratings, k):
  distances = []
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]

  total = 0
  for neighbor in neighbors:
    title = neighbor[1]
    total += movie_ratings[title]
  # Return the average here
  return total / len(neighbors)

###
print(movie_dataset["Life of Pi"])
print(movie_ratings["Life of Pi"])
###

film_pr = predict([0.016, 0.300, 1.022], movie_dataset, movie_ratings, 5)
print(film_pr)
