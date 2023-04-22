# Подкласс встроенного типа/класса list.
# Отображает диапазон 1..N на 0..N-1; вызывает встроенную версию.

class MyList(list):
    def __getitem__(self, offset):
        print('Indexing {0} at {1}'.format(self, offset))
        return list.__getitem__(self, offset - 1)


if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc')
    print(x)
    print()
    print(x[1])
    print(x[3])
    x.append('spam')
    print(x)
    print()
    x.reverse()
    print(x)
    print()
