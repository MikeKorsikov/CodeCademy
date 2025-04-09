# project on classes

# 1-6
class School:
  def __init__(self, name, level, numberOfStudents):
    self.name = name
    self.level = level
    self.numberOfStudents = numberOfStudents
  
  def getName(self):
    return self.name
  
  def getLevel(self):
    return self.level
  
  def getnumberOfStudents(self):
    return self.numberOfStudents
  
  def setnumberOfStudents(self, newNumberOfStudents):
    self.numberOfStudents = newNumberOfStudents

  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students"

#7
s1 = School("First", "middle", 200)
print(s1)
print(s1.getName())
print(s1.getLevel())
print(s1.getnumberOfStudents())
s1.setnumberOfStudents(250)
print(s1.getnumberOfStudents())

#8-13
class PrimarySchool(School):
  def __init__(self, name, numberOfStudents, pickupPolicy):
    super().__init__(name, "primary", numberOfStudents)
    #self.name = name
    #self.numberOfStudents = numberOfStudents
    self.pickupPolicy = pickupPolicy
  
  def getpickupPolicy(self):
    return self.pickupPolicy
  
  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students. Pickup policy: {self.pickupPolicy}"

# 14
s2 = PrimarySchool("Second", 300, "After 15:00")
print(s2)
print(s2.getpickupPolicy())

# 15
class HighSchool(School):
  def __init__(self, name, numberOfStudents, sportsTeams):
    super().__init__(name, "high", numberOfStudents)
    self.sportsTeams = sportsTeams # str
  
  def getsportsTeams(self):
    return self.sportsTeams
  
  def __repr__(self):
    return f"A {self.level} school named {self.name} with {self.numberOfStudents} students. Sports teams: {self.sportsTeams}"

# 16
s3 = HighSchool("Third", 400, "Football, box")
print(s3)
print(s3.getsportsTeams())
