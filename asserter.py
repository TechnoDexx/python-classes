def f(x):
    assert x < 0, 'x must be negative'
    return x ** 2


if __name__ == '__main__':
    x = 1
    try:
        print(f(x))
    except AssertionError as exc:

        print('{0}. Try negative argument for function f({1}):'.format(exc.args[0], x))
        x = -1
        print('Square of {0} is {1}'.format(x, f(x)))
    print('Done')
