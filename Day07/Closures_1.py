
def outer_func():
	message = "hi"

	def inner_func():
		print(message)

	return inner_func()     #, adding a prynthesis means you are executing this function. you need to add prynthesis at the end of it.


outer_func() 



# how, if we want to print without executing it. 

def outer_func():
	message = "hi"

	def inner_func():
		print(message)

	return inner_func    #, adding a prynthesis means you are executing this function. you need to add prynthesis at the end of it.


print(outer_func())   #this will give you someting wierd result. 



#  but what if we add make another variable and equal it to outer_func() 
def outer_func():
	message = "hi"

	def inner_func():
		print(message)

	return inner_func   


result = outer_func() 
print(result)         #still give the same result. But out of two functions, it always becomes the inner function. 

result()    #since it's become the inner function, we can just simply call the function and it will give the result 'hi'

print(result.__name__)  #to find what function it has become, just type this. 


#take aways: when you assign a variable to the outer function, it will always become the inner function. 


def outer_func(message):

	def inner_func():
		print(message)

	return inner_func

hello_func = outer_func('hello')
hi_func = outer_func('hi')


hello_func() 

