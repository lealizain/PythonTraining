'''

1.What are the two values of the Boolean data type? How do you write them?
True and False 

as conditions, you can write them as:

if True: 
or 
if False: 


2. What are the three different types of Boolean operators?
And
Or 
Not

3. Make a list of each Boolean operator's truth tables 
(i.e. every possible combination of Boolean values for the operator and what it evaluate ).
for Flase
1) false
2) none
3) 0
4) '', [], {}, ()

for True 
if it's not any of the above then it's True

4. What are the values of the following expressions?
(5 > 4) and (3 == 5)- False
not (5 > 4)- false
(5 > 4) or (3 == 5)- True
not ((5 > 4) or (3 == 5))- False
(True and True) and (True == False)- False
(not False) or (not True)- True

5. What are the six comparison operators?
==
!=
>
<
<=
>=

is

6. How do you tell the difference between the equal to and assignment operators?

equal to operator is == it is used to compare two values
assignment operator is = it is used to assign a value to variable. 

Describe a condition and when you would use one.
When we write a code, we can give it conditions, so python can evaluate the condition and give the conditioned output.
These conditions are usually in the form of comparison and in True or False. 
We can specify in code, what will happen if the condition is not met (False) or if it is met (True). 

7. Write and Identify the three blocks in this code:

spam = 0
if spam == 10:
print('eggs')
if spam > 5:
print('bacon')
else:
print('ham')
print('spam')
print('spam')

You need to indent after colon of if condition, add elif in the second condition, I don't understand wny you need to print spam twice at the end. Corrent code is below: 
spam = 0
if spam == 10:
	print('eggs')
elif spam > 5:
	print('bacon')
else:
	print('ham')
	# print('spam')
	# print('spam')

8. Write code that prints Hello if 1 is stored in spam, prints Hey if 2 is stored in spam, and prints
Greetings! if anything else is stored in spam.

spam = 3 
if spam ==1:
	print("Hello")
elif spam ==2:
	print("Hey")
else:
	print('Greetings!')


9.If your programme is stuck in an endless loop, what keys you’ll press?
Control + C

10. How can you tell the difference between break and continue?
break stops the loop all together (it will show the finished in ms in output). Condinue will not stop the loop, the function will continue to run on the back, even if it's not showing. This can be seen when there is no [Finised in ms] in output. 

11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
in a for loop of range(10) we get numbers from 0 to 9 -- this prints all the numbers without skiping and number.
in range (0,10), we get numbers from 0 to 9-- here we can pick the spicific range within the range via index value. For example we can say range(2,5) and we will only get [2,3,4]
in range(0, 10, 1), we also get 0 to 9 but here in the last argument, we can specify if we want to increment numbers and by how much, since it is 1, it will not skip. 

12. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent
program that prints the numbers 1 to 10 using a while loop.


for i in range(1, 11):
	print(i)

x = 0
while x < 11:
	if x == 11:
		break
	print(x)
	x +=1


13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
You will have to specify the name of the function you are using in the module when you call it, in this case: print(module.bacon())
'''