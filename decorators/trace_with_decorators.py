from decorators.mytools import tracer


class Person:
	@tracer
	def __init__(self, name, pay):
		self.name = name
		self.pay = pay

	@tracer
	def giveRaise(self, percent):
		self.pay = round(self.pay * (1 + percent))

	@tracer
	def LastName(self):
		return self.name.split()[-1]


bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print(sue.pay)
print(bob.LastName(), sue.LastName())
