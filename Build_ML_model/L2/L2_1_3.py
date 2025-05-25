# Hamming Distance

def hamming_distance(pt1, pt2):
  distance = 0
  for i in range(len(pt1)):
    if pt1[i] != pt2[i]:
      distance += 1
    else:
      pass
  return distance

# test 1
print(hamming_distance([1, 2] , [1, 100]))

# test 2
print(hamming_distance([5, 4, 9] , [1, 7, 9]))