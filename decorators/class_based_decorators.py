class decorator:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # args = list(*args)
        for arg in args:
            print('{0}'.format(arg))
        print('-' * 20)
        self.func(*args, **kwargs)


@decorator
def summa(x, y):
    print(x + y)
    return
''

if __name__ == '__main__':
    summa(6, 7)
