
def square(x):
	return x * x   #you have to use the return function here. 


result = square (7)   #we are just defining x here. see that x is just 1 argument. 

print(result)


# now you can also assign a function to a variable. FOr example:

def square (x):
	return x * x
result = square    # here we have assigned a function to a variable. And now this variable becomes a square function.
print(result(6))   # this is using the first class function.

"""Firstclass function: treats functions as first-class citizens. This means the language supports passing functions 
as arguments to other functions, returning them as the values from other functions,
and assigning them to variables or storing them in data structures."""


"""it can pass as arguments to other functions, for example:"""

 # [1,2,3,4,5] ---> [1,4,9,16,25] we want output in a form of square list.


# lst = [1,2,3,4]

# for i in lst:
# 	print(i*i)  #but we need list. We can do this:
	


# def square(x):
# 	return x*x

# lst = [1,2,3,4]

# result = []
# for i in lst:
# 	result.append(square(i))
# 	print(result)   #it's creating a list every time bc of for loop. To fix it just come out of it.
# print(result)

# putting it into a first class function is easy

def square(x):
	return x*x


lst = [1,2,3,4]

def my_sq(func, list_args):   #we need function argumen that it will pass and list of argument. Just indent inside of it. 

	result = []
	for i in lst:
		result.append(square(i))
	return result          #instead of print, we say return and now your function is ready. And now you can add print. 
print(my_sq(square, lst))  #we need two arguments. It should be squre and it needs to be in a list. 

# Why is this helpful?
# we can easily change if we want to find the cube. for example: 


def cube(x):
	return x*x*x

lst = [1,2,3,4]

def my_sq(func, list_args):

	result = []
	for i in lst:
		result.append(func(i))
	return result 
print(my_sq(cube, list))


