# dir() is a built-in function that returns a list of attributes and methods of an object.
class FakeDict:
  pass

fake_dict = FakeDict()
fake_dict.attribute = "Cool"
print(dir(fake_dict))

#

fun_list = [10, "string", {'abc': True}]
type(fun_list)
print(dir(fun_list))

#

print(dir(5))

#

def this_function_is_an_object():
  pass

print(dir(this_function_is_an_object))