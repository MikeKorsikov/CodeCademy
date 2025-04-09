# OOP

class Dog:
  sound = "Woof"

  def __init__(self, name, age):
    self.name = name
    self.age = age

  def bark(self):
    print(Dog.sound)

###

class Employee:
  new_id = 1

  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1
  
  def say_id(self):
    print(f"My id is {self.id}")

e1 = Employee()
e2 = Employee()

e1.say_id()
e2.say_id()

# Inheritance
class Admin(Employee):
  pass

e1 = Employee()
e2 = Employee()
e3 = Admin()

e3.say_id()

# Overriding Methods
class Admin(Employee):
  def say_id(self):
    print("I am an Admin")

e3.say_id()

# super()
class Animal:
  def __init__(self, name, sound="Grrrr"):
    self.name = name
    self.sound = sound

  def make_noise(self):
    print("{} says, {}".format(self.name, self.sound))

class Cat(Animal):
  def __init__(self, name):
    super().__init__(name, "Meow!") 

pet_cat = Cat("Rachel")
pet_cat.make_noise() # Rachel says, Meow!

###

class Admin(Employee):
  def say_id(self):
    # Write your code below:
    super().say_id()    
    print("I am an admin.")

e3 = Admin()
e3.say_id()

# Multiple Inheritance
class Manager(Admin):
  def say_id(self):
    print("I am in charge.")
    super().say_id()

e4 = Manager()
e4.say_id()





