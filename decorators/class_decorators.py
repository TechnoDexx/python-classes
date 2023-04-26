def decorator(cls):
    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

    return Wrapper


@decorator
class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.attr = 'spam'

    def add(self):
        return self.x + self.y


if __name__ == '__main__':
    X = C(6, 7)
    print(X.add())
    print(X.attr)
