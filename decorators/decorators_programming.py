from tracer import tracer


@tracer
def spam(a, b, c):
    print(a + b + c)


@tracer
def eggs(x, y):
    print(x ** y)


if __name__ == '__main__':
    spam(1, 2, 3)
    spam(a=4, b=5, c=6)
    eggs(2, 16)
    eggs(4, y=4)
