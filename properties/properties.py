class Person:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print('fetch...')
        return self._name

    def setName(self, value):
        print('change...')
        self._name = value

    def delName(self):
        print('remove...')
        del self._name

    name = property(getName, setName, delName, "name property docs")


if __name__ == '__main__':
    bob = Person('Bob Smith')
    print(bob.name)
    print()
    bob.name = 'Robert Smith'
    print(bob.name)
    print()
    del bob.name
    print('-'*80)
    sue = Person('Sue Jones')
    print(sue.name)
    print()
    print(Person.name.__doc__)

