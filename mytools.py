import time


def timer(label='', trace=True):
    class Timer:
        def __init__(self, func):
            self.func = func
            self.alltime = 0

        def __call__(self, *args):
            start = time.process_time()
            result = self.func(*args)
            elapsed = time.process_time() - start
            self.alltime += elapsed
            if trace:
                fmt = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(fmt % values)
            return result

    return Timer


if __name__ == '__main__':
    @timer()
    def function(a, b, c):
        print(a + b + c)


    class A:
        def __init__(self, a, b, c):
            self.a = a
            self.b = b
            self.c = c

        @timer(trace=False)
        def add(self):
            print(self.a + self.b + self.c)


    function(1, 2, 3)
    # X = A(1, 2, 3)
    # X.add()
