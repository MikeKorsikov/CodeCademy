# Classes
class Facade:
  pass

# Instantiate the class
facade_1 = Facade()
print(type(facade_1))

# Objects are instances of classes
facade_1_type =type(facade_1)
print(facade_1_type)

# __main__ means that the code is being run directly, 
# not imported from another module

# Class Variables
class Grade:
  minimum_passing = 65

# Methods
class Dog:
  dog_time_dilation = 7

  def time_explanation(self):
    print("Dogs experience {} years for every 1 human year.".format(self.dog_time_dilation))

pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
# Prints "Dogs experience 7 years for every 1 human year."

class Rules:
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

# methods with arguments
