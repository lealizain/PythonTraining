
class Item:
	def calculate_total_price(self, x, y):    #note: methods: functions that are inside the classes. When you have isolated functions with def, they are considered functions. 
	                                    #But when you create the functions inside the classes, they are called methods.
	                                    #add self, otherwise you will see an error. Note: parameter is something that is passed inside the prynthesis.

	                              # pass  #use pass for an empty. 
	                              return x * y
item1 = Item() 
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
# print (item1. calculate_total_price (item1.price, item1.quantity))


item2 = Item()
item2.name = "Laptop"
item2.price = 2000
item2.quantity = 3
# print (item2. calculate_total_price (item2.price, item2.quantity))


class Item:
	def __init__(self, name, price, quantity):  #this is called the constructor, we just created a method that will be applied to all the instances.
		# print(f'an instance is created for: {name}')  #it will print twice because we have two instances. 

		# It is still not perfect bc we are still using the attribute of phone and laptop. We can get rid of it using the following. 

		self.name = name
		self.price = price
		self.quantity = quantity

item1 = Item('Phone', 100, 5) 


item2 = Item('Laptop', 2000, 3)


# print(item1.name)
# print(item2.name)
# print(item1.quantity)
# print(item2.quantity)
# print(item1.price)
# print(item2.price)

class Item:
	def __init__ (self, name, price, quantity):


		self.name = name
		self.price = price
		self.quantity = quantity

	def calculate_total_price(self):

		return self.price * self.quantity

item1 = Item('Phone', 100, 5) 
item2 = Item('Laptop', 2000, 3)

# print(item1.calculate_total_price())


class Item:
	def __init__(self, name: str, price: float, quantity: int):

		#run validations to the received arguments

		assert price >= 0, f'price must be greater than 0'
		assert quantity >= 0, f'price must be greater than 0'

		self.name = name
		self.price = price
		self.quantity = quantity

	def calculate_total_price(self):

		return self.price * self.quantity

item1 = Item('Phone', 100, -1) 
item2 = Item('Laptop', 2000, 3)

print(item1.calculate_total_price())

