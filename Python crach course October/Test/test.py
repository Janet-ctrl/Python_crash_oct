# Question 15
class Person:

	def __init__(self, firstName, lastName, age, email, middleName=''):
		"""Initialize name and age attributes."""
		self.firstName = firstName
		self.lastName = lastName
		self.age = age
		self.email = email
		self.middleName = middleName

# Question 16

p1 = Person('Jane', 'Smith', 27, 'jsmith@yahoo.com', 'Suzan')
#print(f"{p1}")

p2 = Person('Ben', 'Bond', 30, 'bbond@gmail.com', '')
#print(f"{p2}")