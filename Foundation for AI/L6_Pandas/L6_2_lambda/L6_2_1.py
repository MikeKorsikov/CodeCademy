# Lambda

# integer
add_two = lambda my_input: my_input + 2
print(add_two(3)) # Output: 5

# string
is_substring = lambda my_string: my_string in "This is the master string"
print(is_substring('am')) # Output: False
print(is_substring('the')) # Output: True

# string
contains_a = lambda word: "a" in word 
print(contains_a("apple")) # Output: True
print(contains_a("cherry")) # Output: False

# condition
long_string = lambda str: len(str) > 12 

print(long_string("short"))
print(long_string("photosynthesis"))

#