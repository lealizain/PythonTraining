
class Item:
	pay_rate = 0.8  #pay after 20% discount. 

	def __init__(self, name: str, price: float, quantity: int):

		#run validations to the received arguments

		assert price >= 0, f'price must be greater than 0'
		assert quantity >= 0, f'price must be greater than 0'

		self.name = name
		self.price = price
		self.quantity = quantity

	def calculate_total_price(self):

		return self.price * self.quantity

item1 = Item('Phone', 100, 1) 
item2 = Item('Laptop', 2000, 3)

# print(Item.__dict__)		#This will give the attribut to the class level
# print(item1.__dict__)		#this will give the attribute to the instance level
# print(item2.__dict__)


class Item:
	pay_rate = 0.8   #pay after 20% discount. 

	def __init__(self, name: str, price: float, quantity: int):

		#run validations to the received arguments

		assert price >= 0, f'price must be greater than 0'
		assert quantity >= 0, f'price must be greater than 0'

		self.name = name
		self.price = price
		self.quantity = quantity

	def calculate_total_price(self):
		return self.price * self.quantity

	def apply_discount(self):
		self.price = self.price * self.pay_rate   #you need to add self to overide the attribut that belongs to an instance. 

item1 = Item('Phone', 100, 1) 

item1.apply_discount()
print(item1.price)

#if you want to add a different percent of discount to different item. 

item2 = Item('Laptop', 2000, 3)
item2.pay_rate = 0.7      #this will find the attribute in the instance level not the class level.
item2.apply_discount()
print(item2.price)

