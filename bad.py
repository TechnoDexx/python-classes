def gobad(x, y):
    return x / y


def gosouth(x):
    print(gobad(x, 0))


try:
    gosouth(1)
except ZeroDivisionError as ex:
    print('На ноль делить нельзя!')


