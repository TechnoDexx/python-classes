class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2


class SkipIterator:
    def __init__(self, wrapped):
        self.wrapped = wrapped
        self.offset = 0

    def __next__(self):
        if self.offset >= len(self.wrapped):
            raise StopIteration
        else:
            item = self.wrapped[self.offset]
            self.offset += 2
            return item


class SkipObject:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def __iter__(self):
        return SkipIterator(self.wrapped)


class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):
        print('get[{0}]: '.format(i), end='')
        return self.data[i]

    def __iter__(self):
        print('iter=> ', end='')
        self.ix = 0
        return self

    def __next__(self):
        print('next: ', end='')
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, item):
        print('\ncontains: ', end='')
        return item in self.data


if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)
    I = iter(skipper)
    print(next(I), next(I), next(I))
    for x in skipper:
        for y in skipper:
            print(x + y, end=' ')
    print()
    print('~' * 90)
    X = Iters([1, 2, 3, 4, 5])
    print(3 in X)
    for i in X:
        print(i, end='|')
    print()
    print([i ** 2 for i in X])
    print(list(map(bin, X)))
    I = iter(X)
    while True:
        try:
            print(next(I), end=' @ ')
        except StopIteration:
            break
    print()
    X = Iters('spam')
    print(X[0])
    print()
