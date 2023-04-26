def decorator(F):
    def wrapper(*args, **kwargs):
        print('Wrapping function and class method')
        F(*args, **kwargs)

    return wrapper


@decorator
def get_summ(a, b):
    print(a + b)


class C:
    @decorator
    def method(self, x, y):
        print(x + y)


if __name__ == '__main__':
    get_summ(6, 7)
    X = C()
    X.method(6, 7)
