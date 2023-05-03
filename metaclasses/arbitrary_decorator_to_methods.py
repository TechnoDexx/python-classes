# Фабрика метаклассов: применяет любой декоратор ко всем методам класса

from types import FunctionType
from decorators.mytools import tracer, timer


def decorateAll(decorator):
	class MetaDecorate(type):
		def __new__(cls, classname, supers, classdict):
			for attr, attrval in classdict.items():
				if type(attrval) is FunctionType:
					classdict[attr] = decorator(attrval)
			return type.__new__(cls, classname, supers, classdict)
