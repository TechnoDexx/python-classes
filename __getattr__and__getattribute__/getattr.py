class GetAttr:
    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__: 42')
        return 42

    def __getattr__(self, attr):
        print('getattr: ' + attr)
        if attr == '__str__':
            return lambda *args: '[GetAttr str]'
        else:
            return lambda *args: None


class GetAttribute:
    eggs = 88

    def __init__(self):
        self.spam = 77

    def __len__(self):
        print('__len__: 42')
        return 42

    def __getattribute__(self, attr):
        print('getattribute: ' + attr)
        if attr == '__str__':
            return lambda *args: '[GetAttribute str]'
        else:
            return lambda *args: None


for Class in GetAttr, GetAttribute:
    print('\n' + Class.__name__.ljust(50, '='))
    X = Class()
    print(
    X.eggs,
    X.spam,
    X.other,
    len(X))
    # print('X.eggs: {0}'.format(X.eggs.))
    # print('X.spam: {0}'.format(X.spam))
    # print('X.other: {0}'.format(X.other))
    # print('len(X): {0}'.format(len(X)))

    try:
        X[0]
    except Exception:
        print('fail []')

    try:
        X + 99
    except Exception:
        print('fail +')

    try:
        X()
    except Exception:
        print('fail ()')

    X.__call__()
    print(X.__str__())
    print(X)
