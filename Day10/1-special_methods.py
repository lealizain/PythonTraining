

class Employee:
	raise_amt = 1.4
	num_of_emps = 0


	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' +last + '@email.com'
		self.pay = pay

		Employee.num_of_emps += 1


	def fullname(self):
		return '{} {}' .format(self.first, self.last)


	def __repr__(self):
		return f"Employee('{self.first}, {self.last}, {self.pay})"
		

	# def __str__(self):
	# 	return f"({self.fullname}, {self.email})"


emp_1 = Employee('Ali', 'Zain', 500000)
emp_2 = Employee('Test', 'Employee', 120000)

print(emp_1)

# repr(emp_1)
# str(emp_1)

 
