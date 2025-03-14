# List Comprehensions
grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = [grade +10 for grade in grades ]
print(scaled_grades)

# Your code below:
#1
single_digits  = list(range(0,10))
print(single_digits)

#2
for digit in single_digits :
  print(digit)

#3
squares = []

#4
for digit in single_digits:
  squares.append(digit**2)

#5
print(squares)

#6
cubes = [digit ** 3 for digit in single_digits]

#7
print(cubes)
