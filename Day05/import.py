# Keeping it clean. 
 
# You can also import from different places. For example:

import module

greeting = ['hello', 'bye', 'hey', 'hi']

# # note: you need to write module in the find_index function. below:

print(module.find_index(greeting, "hey"))



# you can also shorten the import file name using "as"
# this function will still work even if you chage it's name from greeting.


import module as mo

message = ['hello', 'bye', 'hey', 'hi']

print(mo.find_index(message, "hi"))


# # you can also import a specific function from a file. 
# # now you can call that function without writing the specific name and it will work.
# # you can even shorten the name of this file. 

from module import find_index as fi
message = ['hello', 'bye', 'hey', 'hi']
print(fi(message, "bye"))




# how is it finding 

import sys
print(sys.path)

# it starts locally and then to the next folder and then the whole system.Turtle
# look how to find the path: 

import calendar
print(calendar.__file__)


# you can find inside this file. find leap year

import calendar
print(calendar.isleap(2020))

