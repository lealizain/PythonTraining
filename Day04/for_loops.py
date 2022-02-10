nums = [1,2,3,4,5,6,7]

for i in nums:
	if i ==4: 
# # 		# line 4 is validating that if you get num 4 then the statement

		print ("you win!")
	
# 		continue
# # 		# if you don't want to stop, you can write continue instead and
# # 		# the function will keep going. 


# 	print (i)

	# now writing all the numbers can take some time
	# you can use range function instead of writing all the numbers

# nums = range(list(10))----this will not work bc it's the list of range not range of list. 

nums = list(range(1, 11))
print (nums)

num = list(range(0, 10, 2))
print(num)

for i in range(2):
	print('hello')

#  how is this working?
# for i in [0,1,2,3,4,5,6,7,8,9]:
# 	print ("hello")
# 	# we make i = 0 then that i prints hello and it goes and does the same thing for 1,2,3..
# so whateve numbe you write in the range, it will give that amount of objects.
 
# it will also print others things too: for example 

for i in range(3):
	print(2*3)