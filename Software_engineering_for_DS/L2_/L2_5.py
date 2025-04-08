# Dunder Methods

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

class Meeting:
  def __init__(self):
    self.attendees = []
    
  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)

  # Write your code
  def __len__(self):
    return len(self.attendees)
    
e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
m1 +e1 
m1 + e2
m1 + e3
print(len(m1)) # output is 3

# Abstraction
from abc import ABC, abstractmethod

class AbstractEmployee(ABC):
  new_id = 1
  def __init__(self):
    self.id = AbstractEmployee.new_id
    AbstractEmployee.new_id += 1

  @abstractmethod
  def say_id(self):
    pass

# Write your code below
class Employee(AbstractEmployee):
  def say_id(self):
    print(self.id)

e1 = Employee()
e1.say_id()

# encapsulation

class Employee():
    def __init__(self):
        self.__id = 3
        # Write your code below
        

e = Employee()
print(dir(e))

# Getters, Setters and Deleters
class Employee():
  new_id = 1
  def __init__(self, name=None):
    self.id = Employee.new_id
    Employee.new_id += 1
    self._name = name

  # Write your code below
  def get_name(self):
    return self._name
  
  def set_name(self, name):
    self._name = name
  
  def del_name(self):
    del self._name

e1 = Employee("Maisy")
e2 = Employee()



e1 = Employee("Maisy")
e2 = Employee()
print(e1.get_name())
e2.set_name("Fluffy")
print(e2.get_name())
e2.del_name()
print(e2.get_name())
