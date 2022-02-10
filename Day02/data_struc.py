
# data structure

message = "hello hi"

# every item/ data in variable is stroed as index. 
# index value: 

print(message[1])

# it's a bit difficult so we use data structure 
# list

# each item in the list is stored as index vaue. 

message = ['hello', 'hi', 'bye']
print(message[0:3])

# note that you need square brackets for the list and when you're writing print. 
# also note that you need to write one index value greater to get the value. 



# append-- it just adds a value at the end of it. 

message = ['hello', 'hi', 'bye']
message.append("hey")
print(message)


# insert-- you can add a value in the middle of list

message = ['hello', 'hi', 'bye']
message.insert(0, "hey")
print(message)



# what if we have 2 lists and we want to add the content of the new list to the first list.

message = ['hello', 'hi', 'bye']
greeting = ['hey', 'bye']

message.extend(greeting)
print(message)

# you can also remove an item

message = ['hello', 'hi', 'bye']
greeting = ['hey', 'bye']
message.extend(greeting)
message.remove('hi')
print(message)


# pop

message = ['hello', 'hi', 'bye']
message.pop('hi')
print(message)


# it will give you an error. You need to write an int in the pop function.
# pop remembers what it removed. 

message.pop(0)

removed = message.pop(1)
print(message)
print(removed)

# in operator-- it helps you to find if the item is present in the list or not.

message = ['hello', 'hi', 'bye']
print("hi" in message) 

# it will give you boolian value. 


# for loop

message = ['hello', 'hi', 'bye']
for i in message:
	print(i)

# how does the for loop work?
# i goes to the index 0 which is present in message- value is true
# Then it print that i. 
# i then goes to index 1 ('hi'), it is present in the message. True statment. 
# Then it print that i again. 
# It does it until it gets a false value.

if True:
	print("the statement was True")

# Now what if we want to find the value of index also. 
# To do this we use a function called enumerate. 

greeting = ['hello', 'hi', 'bye']
for message in enumerate(greeting):
	print(message)

# or 

greeting = ['hello', 'hi', 'bye']
for index, message in enumerate(greeting):
	print(index, message)

# message is just i. 
# remember that you need to add the colon at the end.


# Now what if we want to convert this list into string. How do we do this?
# we use the function called .join and join it with string

greeting = ['hello', 'hi', 'bye']

greeting_str = ' - '.join(greeting)
print(greeting_str)

# # Now if we want to convert the string into list, we use split operator.

greeting_str = greeting_str.split(' ')
print((greeting_str))

# tupple = immutable 

tupple_1 = ('hello', 'hi', 'bye')
tupple_2 = (tupple_1)

print(tupple_1)
print(tupple_2)

tupple_1[0] = 'hey'

print(tupple_1)
print(tupple_2)

# it's giving an error because they are immutable and it does not support item assignment. 


# Sets. it will only write the unique items. write inside the curly item


# sets = {'hello', 'hi', 'bye', 'hey', 'bye', 'Hello'}
# print (sets)

# to find the if something is present in a set. 

# sets = {'hello', 'hi', 'bye', 'hey', 'bye', 'Hello'}
# print ('bye' in sets)
