
class Item:
	pay_rate = 0.8  #pay after 20% discount. 

	all = []

	def __init__(self, name: str, price: float, quantity: int):

		#run validations to the received arguments

		assert price >= 0, f'price must be greater than 0'
		assert quantity >= 0, f'price must be greater than 0'

		self.name = name
		self.price = price
		self.quantity = quantity

		# Actions to execute
		Item.all.append(self)

	def calculate_total_price(self):

		return self.price * self.quantity

	def apply_discount(self):
		self.price = self.price * self.pay_rate

	def __repr__(self):    #to make a nice list to read print(Item.all)
		return f"Item('{self.name}', {self.price}. {self.quantity})'"


item1 = Item('Phone', 100, 1) 
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 2)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)

	

# for instance in Item.all:
# 	print(instance.name)    # To display all the names in all your instances, you can use a for loop


print(Item.all)


