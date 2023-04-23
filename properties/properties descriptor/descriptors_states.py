class DescState:
	def __init__(self, value):
		self.value = value

	def __get__(self, instance, owner):
		print('DescState get')
		return self.value * 10

	def __set__(self, instance, value):
		print('DescState set')
		self.value = value


class InstState:
	def __get__(self, instance, owner):
		print('InstState  get')
		return instance._Y * 100

	def __set__(self, instance, value):
		print('InstSate set')
		instance._ = value


# Клиентский класс
class CalcAttrs:
	X = DescState(2)
	Y = 3

	def __init__(self):
		self.Z = 4


# Клинетский класс
class CalcAttrs_2:
	X = DescState(2)
	Y = InstState()

	def __init__(self):
		self._Y = 3
		self.Z = 4


def Attr_2():
	global obj
	obj = CalcAttrs_2()
	print(obj.X, obj.Y, obj.Z, sep=', ')
	print()
	obj.X = 5
	obj._Y = 6
	obj.Z = 7
	print(obj.X, obj.Y, obj.Z, sep=', ')


def Attr_1():
	global obj
	obj = CalcAttrs()
	print(obj.X, obj.Y, obj.Z, sep=', ')
	obj.X = 5
	obj.Y = 6
	obj.Z = 7
	print(obj.X, obj.Y, obj.Z, sep=', ')


if __name__ == '__main__':
	Attr_1()
	print('|' * 80)
	Attr_2()
