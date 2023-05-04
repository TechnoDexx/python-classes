# Фабрика метаклассов: применяет любой декоратор ко всем методам класса

from types import FunctionType
from decorators.mytools import tracer, timer


def decorateAll(decorator):
	class MetaDecorate(type):
		def __new__(cls, classname, supers, classdict):
			for attr, attrval in classdict.items():
				if not __debug__:
					print('attr: {0}\t\t attrval: {1}'.format(attr, attrval))
				if type(attrval) is FunctionType:
					classdict[attr] = decorator(attrval)
			return type.__new__(cls, classname, supers, classdict)

	return MetaDecorate


class Person(metaclass=decorateAll(tracer)):
	def __init__(self, name, pay):
		self.name = name
		self.pay = pay

	def giveRaise(self, percent):
		return round(self.pay * (1 + percent))

	def lastName(self):
		return self.name.split()[-1]


class AnotherPerson(metaclass=decorateAll(timer(label='[tmr]>'))):
	def __init__(self, name, pay):
		self.name = name
		self.pay = pay

	def giveRaise(self, percent):
		return round(self.pay * (1 + percent))

	def lastName(self):
		return self.name.split()[-1]


"""
Теперь, чтобы применить другой декоратор, нам достаточно будет просто за-
менить имя декоратора в заголовке инструкции class. Например, чтобы вос-
пользоваться декоратором функций timer, показанным ранее, мы могли бы при
определении нашего класса использовать любую из двух последних строк за-
головков, приведенных ниже, – первая из них применяет декоратор timer со
значениями аргументов по умолчанию, а вторая задает текст в аргументе label:
class Person(metaclass=decorateAll(tracer)):  # Применяет tracer
class Person(metaclass=decorateAll(timer())): # Применяет timer, со значениями аргументов по умолчанию
class Person(metaclass=decorateAll(timer(label=’**’))): # Декоратор с аргументами
"""
if __name__ == '__main__':
	bob = Person('Bob Smith', 50000)
	sue = Person('Sue Jones', 100000)
	print(bob.name, sue.name)
	sue.giveRaise(.10)
	print(sue.pay)
	print(bob.lastName(), sue.lastName())
	print('-' * 80)
	bob = AnotherPerson('Bob Smith', 10000)
	sue = AnotherPerson('Sue Jones', 50000)
	print(bob.name, sue.name)
	sue.giveRaise(.30)
	print(sue.pay)
	print(bob.lastName(), sue.lastName())
	print('-' * 80)
	print('{0:5f}'.format(AnotherPerson.__init__.alltime))
	print('{0:5f}'.format(AnotherPerson.giveRaise.alltime))
	print('{0:5f}'.format(AnotherPerson.lastName.alltime))
