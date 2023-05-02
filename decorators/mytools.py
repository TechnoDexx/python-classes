import time


def timer(label='', trace=True):
    def OnDecorator(func):
        def OnCall(*args, **kwargs):
            start = time.process_time()
            result = func(*args, **kwargs)
            elapsed = time.process_time() - start
            OnCall.alltime += elapsed
            if trace:
                fmt = '%s %s: %.5f, %.5f'
                values = (label, func.__name__, elapsed, OnCall.alltime)
                print(fmt % values)
            return result

        OnCall.alltime = 0
        return OnCall

    return OnDecorator


if __name__ == '__main__':
    @timer(label='[CCC]==>')
    def listcomp(N):
        return [x * 2 for x in range(N)]

    @timer(trace=True)
    def function(a, b, c):
        print(a + b + c)


    class A:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        @timer(label='>>', trace=True)
        def add(self):
            print(self.a + self.b + self.c)


    function(1, 2, 3)
    X = A(1, 2, 3)
    X.add()
    print(listcomp(1000))
