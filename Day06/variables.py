
x = 'global x'


def demo():
	y = 'local y'     #anything inside the demo() is part of the def function.
	print(x)          # it's not going to print, bc you need to run the defined function

demo()                # it will print the global x not local y. 

def demo():
	y = "local y"
	print(y)
demo()


# This is happening because of LEGB- local, enclosing, global, builtins
x = 'global x'

def demo():
	x = "local x"
	print(x)
demo()              #it will print out local x and not global x bc there is x in the local
print(x) #with this you'll see both local x and global x in respective.


# # you can also make a global variable inside local variable. For example:

def demo():
	global x   #here, but avoid using it. it's witten before writing the x variable. 

	x = "local x"
	      
	print(x)
demo()  


 

def demo():
	y = "local y"
	print(y)
demo()

to import builtins

import builtins

print(dir(builtins))    #this will show you all the builtin functions

nums = [5,2,4,12,3,1,51]

print(max(nums))         #max is a builtin function


print(help(max(nums)))    #it will give you what the function is all about. 


import builtins

def max():   #this is an empty argument
	pass
nums = [5,2,4,12,3,1,51]
print(max(nums)) 
max()
It gave an error bc when we defined max it was empty argument but when we printed it there is 1 orgument.

def outer():
	x = 'outer x'

	def innner():
		x = 'inner x'
		print(x)
	print(x)
outer()       

# why is it only giving one print?
# we have to run the function twice for 2 def function at thier respective places.

def outer():
	x = 'outer x'

	def inner():
		x = 'inner x'
		print(x)
	inner()

	print(x)    #this print is for the outer function

outer()













