class PrivateExc(Exception):  # Подробнее об исключениях позднее
    pass


class Privacy:
    def __init__(self):
        self.privates = []

    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivateExc(self, attrname)
        else:
            self.__dict__[attrname] = value


class Test1(Privacy):
    privates = ['age']


class Test2(Privacy):
    privates = ['name', 'pay']

    def __init__(self):
        self.__dict__['name'] = 'Tom'


def self_test():
    x = Test1()
    y = Test2()
    x.name = 'Bob'
    y.name = 'Sue'  # Ошибка
    y.age = 30
    x.age = 40  # Ошибка


if __name__ == '__main__':
    self_test()
