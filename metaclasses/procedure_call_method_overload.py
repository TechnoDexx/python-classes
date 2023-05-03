# Метод __call__ можно переопределить,
# а метаклассы могут иметь свои метаклассы

class SuperMeta(type):
	def __call__(cls, classname, supers, classdict):
		print('In SuperMeta.call: ', classname, supers, classdict, sep='\n...')
		return type.__call__(cls, classname, supers, classdict)


class SubMeta(type, metaclass=SuperMeta):
	def __new__(cls, classname, supers, classdict):
		print('In SubMeta.new: ', classname, supers, classdict, sep='\n...')
		return type.__new__(cls, classname, supers, classdict)

	def __init__(cls, classname, supers, classdict):
		print('In SubMeta init:', classname, supers, classdict, sep='\n...')
		print('... init class object: ', list(cls.__dict__.keys()))


class Eggs:
	pass


print('Making Class...')


class Spam(Eggs, metaclass=SubMeta):
	data = 1

	def meth(self, args):
		pass


print('Making Instance...')

X = Spam()

print('data: ', X.data)
