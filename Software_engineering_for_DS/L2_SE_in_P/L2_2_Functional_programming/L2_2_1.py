# Functional Programming

# Immutable Data types 
from collections import namedtuple

country = namedtuple("country", ["name", "capital", "continent"])

# Checkpoint 1 code goes here.
france = country("France", "Paris", "Europe")
# Checkpoint 2 code goes here.
japan = country("Japan", "Tokyo", "Asia")
# Checkpoint 3 code goes here.
senegal = country("Senegal", "Dakar", "Africa")

countries = (france, japan, senegal)