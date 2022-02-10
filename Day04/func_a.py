

# def demo_func():
# 	print('hello')

# # when you write this function only, it will not run because:
# # you have only defined the function. You also need to execute it. 
# # To execute: write the demo_func() below

	# demo_func()

# reason to do this: 
# for example: you have written print ("hello") 100 times

# print("hello")
# print("hello")
# print("hello")
# print("hello")
# print("hello")

# how you want to change that hello and add ! also. 
# By defining it you can change it quickly. 

# def demo_func():
# 	print('hello!')

# demo_func()
# demo_func()
# demo_func()
# demo_func()
# demo_func()



# Return function

def demo_func():
	a = 1 
	b = 2
	result = a + b
	return result

demo_func()

# here we have calculated the result, and python has gotten the answer. we need to ask python to print the result.

print(demo_func())



def new_func(greeting):
	message = greeting

	return message

print(new_func("hello"))

# or an easy way to do this is just cancle the message line

def new_func(greeting, message):

	return f'{greeting}--- {message}'

print(new_func("hello", "Morning"))