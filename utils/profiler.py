import cProfile


def profiler(label='', trace=True):
    def OnDecorator(func):

        def OnCall(*args, **kwargs):
            print('Profiling function named {0} : \n'.format(func.__name__))
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
    @profiler(trace=True)
    def traced_function(a, b, c):
        print(a + b + c)

    class A:
        @profiler(trace=False)
        def traced_method(self, a, b, c):
            return print(a + b + c)
        

    traced_function(1, 2, 3)
    X = A()
    X.traced_method(1, 2, 3)
