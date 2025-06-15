# classification
# K-Nearest Neigbors (KNN) - classification algorithm

star_wars = [125, 1977, 11000000]
raiders = [115, 1981, 18000000]
mean_girls = [97, 2004, 17000000]

def distance(movie1, movie2):
    total = 0
    for i in range(len(movie1)):  # Loop through each dimension
        diff = movie1[i] - movie2[i]
        total += diff ** 2
    return total ** 0.5  # Square root of the sum of squared differences

#
print(distance(star_wars, raiders))
print(distance(star_wars, mean_girls))

###

# Data with Different Scales: Normalization (step 1)

release_dates = [1897, 1998, 2000, 1948, 1962, 1950, 1975, 1960, 2017, 1937, 1968, 1996, 1944, 1891, 1995, 1948, 2011, 1965, 1891, 1978]

# 1
def min_max_normalize(lst):
    minimum = min(lst)  # Find the smallest value in the list
    maximum = max(lst)  # Find the largest value in the list

    # 2
    normalized = []     # Store normalized values here
    
    for value in lst:
        # Apply min-max normalization formula: (value - min) / (max - min)
        normalized_value = (value - minimum) / (maximum - minimum)
        normalized.append(normalized_value)
    
    return normalized

# 3
sample = min_max_normalize(release_dates)

print(sample)

###

# Finding the Nearest Neighbor (step 2)

from movies import movie_dataset, movie_labels

print(movie_dataset['Bruce Almighty'])
print(movie_labels['Bruce Almighty'])

def distance(movie1, movie2):
  squared_difference = 0
  for i in range(len(movie1)):
    squared_difference += (movie1[i] - movie2[i]) ** 2
  final_distance = squared_difference ** 0.5
  return final_distance

def classify(unknown, dataset, k):
  distances = []

  for title in dataset:
    data_point = dataset[title]  # Get the features (e.g., [runtime, year])
    distance_to_point = distance(unknown, data_point)  # Compute distance
    distances.append([distance_to_point, title])  # Store distance and title
  
  distances.sort()
  neighbors = distances[:k]
  return neighbors 

test_1 = classify ([.4, .2, .9], movie_dataset, 5)
print(test_1)

###

# Classify the new point based on those neighbors (step 3)

def classify(unknown, dataset, labels, k):
  distances = []
  num_good = 0
  num_bad = 0
  #Looping through all points in the dataset
  for title in dataset:
    movie = dataset[title]
    distance_to_point = distance(movie, unknown)
    #Adding the distance and point associated with that distance
    distances.append([distance_to_point, title])
  distances.sort()
  #Taking only the k closest points
  neighbors = distances[0:k]

  # 2
  for movie in neighbors:
    title = movie[1]
  #return title

  # 3
    if labels[title] == 1:
      num_good += 1
    else:
      num_bad += 1
  # 4 Return classification decision
  return 1 if num_good > num_bad else 0

# testing function
test_3 = classify([.4, .2, .9], movie_dataset , movie_labels , 5)
print(test_3)

