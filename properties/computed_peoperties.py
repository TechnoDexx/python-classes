class PropSquare:
    def __init__(self, start):
        self.value = start

    def getX(self):
        return self.value ** 2

    def setX(self, value):
        self.value = value

    X = property(getX, setX)


if __name__ == '__main__':
    P = PropSquare(3)
    Q = PropSquare(32)
    print(P.X)
    P.X = 4
    print()
    print(P.X)
    print()
    print(Q.X)
