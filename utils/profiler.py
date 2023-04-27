import cProfile


def profiler(F):
    def wrapper(*args, **kwargs):
        print('Profiling function named {0} : \n'.format(F.__name__))
        prof = cProfile.Profile()
        prof.enable()
        F(*args, **kwargs)
        prof.disable()
        print(prof.print_stats())

    return wrapper


if __name__ == '__main__':
    import sys
    import os

    if sys.gettrace():
        os.system('clear')


        @profiler
        def S(a, b):
            print('S result: {0}'.format(a + b))
            print()


        S(5, 6)


        class A:
            @profiler
            def method(self, x, y):
                print('method result: {0}'.format(x ** y))
                print()


        Z = A()
        Z.method(2, 3)
    else:
        print('Use Debug Mode for showing Result')
