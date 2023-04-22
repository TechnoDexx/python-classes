class Set(list):
    def __init__(self, value=None):
        if value is None:
            value = []

        list.__init__([])
        self.concat(value)

    def intersect(self, other):
        res = []
        for x in self:
            if x in other:
                res.append(x)
        return Set(res)

    def union(self, other):
        res = Set(self)
        res.concat(other)
        return res

    def concat(self, value):
        for x in value:
            if x not in self:
                self.append(x)

    def __and__(self, other):
        return self.intersect(other)

    def __or__(self, other):
        return self.union(other)

    def __repr__(self):
        return 'Set: ' + list.__repr__(self)


if __name__ == '__main__':
    x = Set([1, 3, 5, 7])
    y = Set([2, 1, 4, 5, 6])
    print('{0}, {1} \n\tlen({0}) = {2}'.format(x, y, len(x)))
    print()
    print('{0}.intersect({1})={2}, {1}.union({0})={3}'.format(x, y, x.intersect(y), y.union(x)))
    print()
    print('{0} & {1} = {2}\n{0} | {1} = {3}'.format(x, y, x & y, x | y))
    print()
    x.reverse()
    print(x)
