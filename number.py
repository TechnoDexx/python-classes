class Number:
    """
    """

    def __init__(self, start):
        self.data = start

    def __sub__(self, other):
        return Number(self.data - other)

    def __str__(self):
        return str(self.data)


class Indexer:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, item):
        print('getitem: ', item)
        return self.data[item]

    def __setitem__(self, key, value):
        self.data[key] = value
        return self.data

    def __str__(self):
        return str(self.data)


def self_test():
    X = Number(5)
    Y = X - 2
    # print('Y.data = {0}'.format(Y.data))
    print(Y)


if __name__ == '__main__':
    self_test()
