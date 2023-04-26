def decorator(F):
    def wrapper(*args):
        for arg in args:
            print('{0}'.format(arg))      # Использование F и аргументов
        print('-' * 20)
        F(*args)                          # F(*args) - вызовы оригинальной функции

    return wrapper


@decorator
def summa(a, b):
    print(a + b)
    # return


if __name__ == '__main__':
    summa(6, 7)
