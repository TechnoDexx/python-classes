from access import Public, Private


@Private('age')
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


X = Person('Bob', 40)
print(X.name)
print(X.age)
X.name = 'Sue'
print(X.name)
