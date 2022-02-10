bacon = 22
bacon + 1

print(isinstance(bacon, int))

x = 'spam' * 3 
print(x)




x= 'I have eaten' + 99 + 'burritos.'
print (x)




greeting= "Hello"
message = "Morning"
g_m = '{}, Good {}'.format(greeting, message)
print(g_m)

# or

g_m = f"{greeting}, good {message}"
print(g_m)





spam = 1
if spam == 10:
	print('eggs')
if spam > 5:
	print('bacon')
else:
	print('ham')
	print('spam')
	print('spam')

8. Write code that prints Hello if 1 is stored in spam, prints Hey if 2 is stored in spam, and prints
# Greetings! if anything else is stored in spam.

spam = 3 
if spam ==1:
	print("Hello")
elif spam ==2:
	print("Hey")
else:
	print('Greetings!')





n = list(range(10))
print(n)
nums = list(range(2, 5))
print (nums)
num = list(range(0, 10, 4))
print(num)







x = 0
while x < 11:
	if x == 11:
		break
	print(x)
	x +=1

for i in range(1, 11):
	print(i)







x = 0

while x < 10:
	if x ==10:
		 break
		# continue
	print(x)
	x+=1





spam = 2
if spam == 10:
print('eggs')
elif spam > 5:
	print('bacon')
else:
	print('ham')
	print('spam')
	print('spam')

