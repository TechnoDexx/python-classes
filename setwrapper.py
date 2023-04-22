class Set:
    def __init__(self, value=None):
        if value is None:
            value = []
        self.data = value
        self.concat(value)

    def intersect(self, other):
        res = []
        for __x in self.data:
            if __x in other:
                res.append(__x)
        return Set(res)

    def union(self, other):
        res = self.data[:]
        for __x in other:
            if __x not in res:
                res.append(__x)
        return Set(res)

    def concat(self, value):
        for __x in value:
            if __x not in self.data:
                self.data.append(__x)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        return self.data[key]

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return 'Set:' + repr(self.data)


if __name__ == '__main__':
    x = Set([1, 3, 5, 7])
    # noinspection PyTypeChecker
    print(x.union(Set([1, 4, 7])))  # Выведет: Set:[1, 3, 5, 7, 4]
    # noinspection PyTypeChecker
    print(x | Set([1, 4, 6]))       # Выведет: Set:[1, 3, 5, 7, 4, 6]
