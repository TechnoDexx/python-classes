class Discover:
    __slots__ = ['name', 'age']

    def discover(self):
        for x in self.__slots__:
            if x is not None:
                print(x)


class B(Discover):
    __slots__ = ['gender'] + Discover.__slots__

    def discover(self):
        Discover.discover(self)


if __name__ == '__main__':
    A = Discover()
    print(A.discover())
    print()
    B = B()
    print(B.discover())
    print()
    B.name = "Eric"
    B.age = 25
    B.gender = 'Male'
    print()
    B.salary = 500000  # Возбуждается исключение AttributeError. Такого параметра нет в списке __slots__ класса.
