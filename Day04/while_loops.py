
# x = 0

# while x < 10:
# 	print("hello") 

# don't do this, because x will always be less than 10
# you will get infinity number of hello
# to end the loop, you need to increment it by 1
# now: 

# x = 1

# while x < 10:
# 	print("hello")
# 	x += 1

# 	how is the incrementing working?

# 		When x becomes 10 the while condition became false.
# 		When the condition became false, it stoped. 


x = 0

while x < 10:
	if x ==10:
		 break
		# continue
	print(x)
	x+=1


# What is happening here? it gave you 5 results
# line 26: x is less than 10->true statement. 
# line 28: We wrote that if x is equal to 5 than break. this statement i false for x=0
# Line 29: we print x
# Line 30: We now increment x by 1, and now x is 1. 
# when we reach value where x== 5 we break. and the statemtent is false and the result will not be printed. 

# You can also use continue statement, instead of break. 
# This will stop wring until number 4, but the program is still running. 
