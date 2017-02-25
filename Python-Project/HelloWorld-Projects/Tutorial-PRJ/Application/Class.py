class Employee:

	raise_rate = 1.04

	def __init__(self, firstName, LastName, City,Salary):
		self.first = firstName
		self.last = LastName
		self.email = firstName + '.' + LastName + '@company.com'
		self.City = City
		self.Salary = Salary


	def FullName(self):
		return '{} {}'.format(self.first, self.last)

	def BonusRate(self):
		return self.Salary * Employee.raise_rate

	def Address(self):
		return self.City




HR = Employee('Prajwol','Thapa','Kathmandu',2000)
HR2 = Employee('Ojashri','Thapa','Sydney',5000)

HR.raise_rate =2.0

print (HR.raise_rate)
print (HR2.raise_rate)

print(Employee.__dict__)
print (Employee.__init__)