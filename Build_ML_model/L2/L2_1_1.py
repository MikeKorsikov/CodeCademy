# Supervised Learning: Regression

# Regression is used to predict outputs that are continuous.
# Classification is used to predict a discrete label.

def euclidean_distance(pt1, pt2):
  distance = 0
  for point in range(len(pt1)):
    distance = distance + (pt1[point] - pt2[point]) ** 2
  distance = distance ** (1/2) #square the difference
  return distance

# test 1:
a = [1, 2] 
b = [4, 0]

dist1 = euclidean_distance(a,b)
print(dist1)

# test 2
c = [5, 4, 3]
d = [1, 7, 9]

dist2 = euclidean_distance(c,d)
print(dist2)