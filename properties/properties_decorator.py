class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """name property docs"""
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):
        print('change...')
        self._name = value

    @name.deleter
    def name(self):
        print('remove...')
        del self._name


if __name__ == '__main__':
    bob = Person('Bob Smith')
    print(bob.name)
    print()
    bob.name = "Robert Smith"
    print(bob.name)
    del bob.name
    bob.name = 'Bob Smith'
    print()
    print(bob.name)
    print('-'*80)
    sue = Person('Sue Jones')
    print(sue.name)
    print(Person.name.__doc__)
