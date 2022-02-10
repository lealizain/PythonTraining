
def decorator_function(func):
	def wrapper_function():
		print('hello')
		return func()
	return wrapper_function



def display():
	print('function ran!')


decorated_disp = decorator_function(display)    #when you assign a outer function to a variable, it will become inner function. 
decorated_disp()     #hello will also get printed out. 