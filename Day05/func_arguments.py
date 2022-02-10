
# def demo_func(greeting, name):
#  return f"{greeting} -- {name}"

# # demo_function is taking the argument (greeting) and accessing that variable {"greeting"}.

# print(demo_func("hello", "Ali"))



# # now, you can predefined a variable, for example:

def demo_func(greeting, name= "ali"):
 return f"{greeting} -- {name}"

print(demo_func("hello"))



# # you can still get another argument.

print(demo_func("hello", "Zain"))

# # if you have more than two arguments, it will give an error. 

# # print(demo_func("hello", "zain", "bye", "take care"))

# # To pass multiple arguments, you can add a list. Ex:

print(demo_func(["hello", "zain", "bye"], "take care"))



# star arguments (*) and kewarg arguments aka dictionary(**)

def emp_info(*args, **kwargs):
	print(args)
	print(kwargs)

print(emp_info("hello", "hi", "bye", name = "John", age= 27))

# kwargs argument: it has taken it as a tuple and it's nothing but a dictionary.
# if you remove stars and double stars, it will give you an error.
