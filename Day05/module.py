
# ['hello', 'bye', 'hey', 'hi']

# exercise: we need to define a function so it gives you the index value.
# you need 2 things in oder to find the index value of bye. 
# 1: loops 
# 2: conditions

# this function will take two arguments:
# 1: to_search
# 2: target (what you're looking for)

# def find_index(to_search, target)
# you need to wite in enumerate



greeting = ['hello', 'bye', 'hey', 'hi']


for i, v in enumerate(greeting):
	print(i)

# 	# it will only give index nuumbers, to get the values: 
# 	print(i,v)

# this is the first part. Now you need to add a condition in it.



greeting = ['hello', 'bye', 'hey', 'hi']

for i, v in enumerate(greeting):
	if v == "bye":
		return i 
	print(-1)

# this will give you an error. return is outside of function





greeting = ['hello', 'bye', 'hey', 'hi']
def find_index(to_search, target):
	for index, value in enumerate(greeting):
		if value == target:
			return index
	return -1
	
# print(find_index(greeting, "hi"))

# # line 50: you don't have to write else. You also don't have to write -1, you can write anything. 
# line 50: remember that you need to write return as a part of for, nor if.




