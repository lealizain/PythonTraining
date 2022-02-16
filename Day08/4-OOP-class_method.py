class Employee:
	raise_amt = 1.4
	num_of_emps = 0


	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' +last + '@email.com'
		self.pay = pay

		Employee.num_of_emps += 1 #use it under __init__ becuase number of emp is init. Here you don't need self because you don't need to minipulate/override number of emp


	def fullname(self):
		return '{} {}' .format(self.first, self.last)

	def apply_raise(self):
		self.pay = self.pay * self.raise_amt

	@classmethod
	def set_raise_amt(cls,amount):
		cls.raise_amt = amount 


	@classmethod
	def from_string(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

emp_1 = Employee('Ali', 'Zain', 500000)
emp_2 = Employee('Test', 'Employee', 120000)


emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-80000'
emp_str_3 = 'Jane-Doe-120000'


# first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)













