import cProfile


def profiler(label='', trace=True, isClass=False):
    def OnDecorator(func):
        def OnCall(*args, **kwargs):
            if isClass:
                message = 'Profiling class, named {0} :\n'
            else:
                message = 'Profiling function, named {0} : \n'

            print(message.format(func.__name__))
            prof = cProfile.Profile()
            prof.enable()
            result = func(*args, **kwargs)
            prof.disable()
            if trace:
                print('{0}{1}'.format(label, prof.print_stats()))
            return result

        return OnCall

    return OnDecorator


if __name__ == '__main__':
    @profiler()
    def traced_function(a, b, c):
        print(a + b + c)


    @profiler(isClass=True, label='=>')
    class A:
        def __init__(self, i):
            self.i = i

        def isInt(self):
            return isinstance(self.i, int)

        @profiler(label='==>')
        def traced_method(self, a, b, c):
            return print(a + b + c)


    traced_function(1, 2, 3)
    X = A(0)
    print(X.isInt())
    X.traced_method(1, 2, 3)
