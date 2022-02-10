# import turtle

# my_turtle = turtle.Turtle()



# Inefficent way of making a square.

# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(100)

# DRY - Don't repeat yourself

def square():
	my_turtle.forward(100)
	my_turtle.right(90)
	my_turtle.forward(100)
	my_turtle.right(90)
	my_turtle.forward(100)
	my_turtle.right(90)
	my_turtle.forward(100) 

# At this time this function will not get executed bc we just defined the function.forward
# you just need to execute the defined function. 
# Simply write the function that you have just defined. 

square()
my_turtle.forward(50)
square()
my_turtle.forward(50)
square()
my_turtle.forward(50)
square()

 # Reason to define the function?

 # If we want to repeat something, using the same function, we can define that function. 

# You can also simplify using for-loop the function as below:

def square():

	for i in range(4):
		my_turtle.forward(100)
		my_turtle.right(90)

square()


# You can write inside the defined function. 

def square(length, angle):

	
	my_turtle.forward(length)
	my_turtle.right(angle)
	my_turtle.forward(length)
	my_turtle.right(angle)
	my_turtle.forward(length)
	my_turtle.right(angle)
	my_turtle.forward(length) 

# It will give you an error, until you write the number of length in the square. 
# So, when we execute it we can write the value. 


square(100, 90)

# It is taking argument and executing it. 

# Now you can write it cleaner:

def square (length, angle):

	for i in range(4):
		my_turtle.forward(length)
		my_turtle.right(angle)

	
square(100, 90)

# Now how can we creat 1000 squares? 

# # simply do this:

for i in range(100):
	square(100,90)





# turtle.done()