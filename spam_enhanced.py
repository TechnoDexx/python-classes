class Spam:
    numInstances = 0

    @classmethod
    def count(cls):
        cls.numInstances += 1

    def __init__(self):
        self.count()


class Sub(Spam):
    numInstances = 0

    def __init__(self):
        Spam.__init__(self)


class Other(Spam):
    numInstances = 0


if __name__ == '__main__':
    x = Spam()
    y1, y2 = Sub(), Sub()
    z1, z2, z3 = Other(), Other(), Other()
    print('{0} {1} {2}'.format(x.numInstances, y1.numInstances, z1.numInstances))
    print('{0} {1} {2}'.format(Spam.numInstances, Sub.numInstances, Other.numInstances))
