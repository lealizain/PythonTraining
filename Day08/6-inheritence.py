
class Employee:
	raise_amt = 1.4
	num_of_emps = 0


	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f"{first.lower()}.{last.lower()}@company.com"
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

	@staticmethod
	def is_weekday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True



class Developer(Employee):
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__ (first, last, pay)  #super is going to pass first, last, pay to our Emploee init method. Another way to do this is:

		self.prog_lang = prog_lang  #adding a new init


class Manager(Employee):
 
	def __init__(self, first, last, pay, employees=None):
		super().__init__ (first, last, pay)  
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def revmove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)


	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())

dev_1 = Developer('Ali', 'Zain', 500000, 'Python')
dev_2 = Developer('Test', 'Employee', 120000, 'Java')


mgr_1 = Manager('Sue', 'Smith', 150000, [dev_1])

print(mgr_1.email)
# mgr_1.print_emps()

mgr_1.add_emp(dev_2)
# mgr_1.print_emps()

mgr_1.revmove_emp(dev_2)
mgr_1.print_emps()


# print(help(Developer))

# print(dev_1.email)
# print(dev_1.prog_lang)

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)



# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Developer))   #they don't share same instances because we added Employee in Devoloper class.

# print(issubclass(Developer, Employee))  #Developer is subclass of Employee 
# print(issubclass(Manager, Developer))   #Falce same reason as above



