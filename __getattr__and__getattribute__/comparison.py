class GetAttr:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattr__(self, attr):
        print('get: {0}'.format(attr))
        return 3


X = GetAttr()
print(X.attr1, X.attr2, X.attr3, sep=', ')
print('-' * 80)


class GetAttribute:
    attr1 = 1

    def __init__(self):
        self.attr2 = 2

    def __getattribute__(self, attr):
        print('get: {0}'.format(attr))
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)


X = GetAttribute()
print(X.attr1, X.attr2, X.attr3, sep=', ')
