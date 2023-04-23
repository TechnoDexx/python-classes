# DESCRIPTION:  sd

def raise1(): raise IndexError


def noraise(): return


def raise2(): raise SyntaxError


# TODO:
for func in (raise1, noraise, raise2):
    print('\n', func.__name__, sep=' ')
    try:
        try:
            func()
        except IndexError:
            print('caught IndexError')
        except SyntaxError:
            print('caught SyntaxError')
    finally:
        print('finally run')
