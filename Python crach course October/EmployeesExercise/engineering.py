from employees import Employees

class Engineering(Employees):
	def __init__(self, firstName, lastName, ID, email, role, salary, address=''):
		super().__init__(firstName, lastName, ID, email, address)
		self.role = role
		self.salary = salary

	def displayInfo(self):
		if (self.address):
			print(f"Name: {self.firstName} {self.lastName}")
			print(f"Age: {self.ID}")
			print(f"Email: {self.email}")
			print(f"Email: {self.role}")
			print(f"Email: {self.salary}")
			print(f"Department: {self.address}\n")
		else:
			print(f"Name: {self.firstName} {self.lastName}")
			print(f"Age: {self.ID}")
			print(f"Email: {self.email}")
			print(f"Email: {self.role}")
			print(f"Email: {self.salary}\n")
