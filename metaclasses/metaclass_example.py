class MetaOne(type):
    def __new__(cls, classname, supers, classdict):
        print('In MetaOne.new:', classname, supers, classdict, sep='\n...')
        return type.__new__(cls, classname, supers, classdict)

    """
    Метаклассы могут также переопределять метод __init__, вызываемый мето-
    дом __call__ объекта type: вообще говоря, метод __new__ создает и возвращает
    объект класса, а метод __init__ инициализирует уже созданный класс.
    """

    def __init__(cls, classname, supers, classdict):
        print('In MetaOne init:', classname, supers, classdict, sep='\n...')
        print('...init class object: ', list(cls.__dict__.keys()))


class Eggs:
    pass


print('Making Class..')


class Spam(Eggs, metaclass=MetaOne):
    data = 1

    def meth(self, arg):
        pass


print('Making Instance...')
X = Spam()
print('data: ', X.data)
