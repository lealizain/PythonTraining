"""

1. In the below elements which of them are values or an expression? 
eg:- values can be
integer or string and expressions will be mathematical operators.

* : math operator

'hello' : string

-87.8: float
- : math operator
/ : math operator
+ : math operator
6 : integer

2. What is the difference between string and variable?

variable gives computer to store value/data into its memory. There are many data types that can be stored, string is an example of data type. 

3. Describe three different data types.

list- it is used as a data structure(to minipulate data). It is in order and is mutable. To use it, we use square brackets and put the list init. Ex: [1, 2, 3, 4]
tuple- tuple is very similar to list, but tuple is not mutable (immutable). We don't use square brackets in tuple.
dictionary- dictionary is unordered and mutable and stores maping of keys in values. It is written in curly brackets and elements are seperated by comma. {}

4. What is an expression made up of? What do all expressions do?
Expression is made up of operators, values and variables. Expressions interpret the operators, values, and variables to produce some value that is equal to expression.

5. This assignment statements, like spam = 10. What is the difference between an expression and a statement?
Statement is just a stand alone value of execution and does not return anything. Whereas, expression will takes values, interpret them and give a new value in retun.


6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1

Variable bacon contains integer. 
print(isinstance(bacon, int))-- output = true

7. What should the values of the following two terms be?
'spam' + 'spamspam' : spamspamspam
'spam' * 3 : spamspamspam

8. Why is eggs a valid variable name while 100 is invalid?
well it can cause poblems in coding and it will not make sense if you use digit as a variable name. For example
eggs = 5 
100 = 5

eggs*100 : is it 500 or 25? Not logical and methamatically worng. 


9. What three functions can be used to get the integer, floating-point number, or string version of a value?
int()
float()
str()


10. Why does this expression cause an error? How can you fix it?
'I have eaten' + 99 + 'burritos.'

There is an integer there. Python will add int with int and str with str.
just add a string to 99. You can also add space after eaten, and 99. 

x= 'I have eaten ' + '99 ' + 'burritos.'
print(x)

or 

x= 'I have eaten' 
y= 'burritos.'
print(f"{x} 99 {y}")

create 2 variables message and greeting and assign a values Morning and Hey. Using string representation methods. i.e .format and f'strings' display the output 'Hello, Good Morning'

greeting= "Hello"
message = "Morning"

g_m = '{}, Good {}'.format(greeting, message)
print(g_m)

g_m = f"{greeting}, good {message}"
print(g_m)


