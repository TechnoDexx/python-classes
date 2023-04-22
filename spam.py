class Spam:
    NumInstances = 0

    # TODO: sdfsdf
    def __init__(self):
        Spam.NumInstances = Spam.NumInstances + 1

    def __del__(self):
        Spam.NumInstances = Spam.NumInstances - 1

    @staticmethod
    def printNumInstances():
        return 'Number of instances created: {0}'.format(Spam.NumInstances)


if __name__ == '__main__':
    a = Spam()
    b = Spam()
    c = Spam()
    print(Spam.printNumInstances())
    del a
    print(Spam.printNumInstances())
    del b, c
    print(Spam.printNumInstances())
    print(Spam.printNumInstances())
