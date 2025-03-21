# conservative approach to opening file
fun_cities_file = open('fun_cities.txt', 'a')

# We can now append a line to "fun_cities".
fun_cities_file.write("Montréal")

# But we need to remember to close the file
fun_cities_file.close()


# open file with "with"
with open("welcome.txt") as text_file:
  text_data = text_file.read()

print(text_data)

# iterating lines
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)

# read single line
with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)

# writing to file
with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write("PSB")

# appending file (add at the bottom)
with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write("Air Buddy\n")

# reading CSV
import csv

with open("cool_csv.csv") as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row["Cool Fact"])

