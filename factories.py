def factory(aClass, *args, **kwargs):
    return aClass(*args, **kwargs)


class Spam:
    def doit(self, message):
        print(message)


class Person:
    def __init__(self, name, job):
        self.name = name
        self.job = job

    def __str__(self):
        return '{0} works as a {1}'.format(self.name, self.job)


if __name__ == '__main__':
    object1 = factory(Spam)
    object2 = factory(Person, 'Guido', 'guru')
    object1.doit('Hello, World! I am here!')
    print(object2)
