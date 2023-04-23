class Name:
	"""Name descriptor docs"""

	def __get__(self, instance, owner):
		print('fetch...')
		return instance._name

	def __set__(self, instance, value):
		print('change...')
		instance._name = value

	def __delete__(self, instance):
		print('remove...')
		del instance._name


class Person:
	def __init__(self, name):
		self._name = name

	name = Name()


if __name__ == '__main__':
	bob = Person('Bob Smith')
	print(bob.name)
	print()
	bob.name = 'Robert Smith'
	print(bob.name)
	del bob.name
	print('-' * 80)
	sue = Person('Sue Jones')
	print(sue.name)
	print(Name.__doc__)