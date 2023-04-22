class TraceBlock:
    @staticmethod
    def message(arg):
        print('running', arg)

    def __enter__(self):
        print('starting with block')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            print('exited normally\n')
        else:
            print('Raise an exception:', exc_type)
            return False


if __name__ == '__main__':
    with TraceBlock() as action:
        action.message('Test #1')
        print('Reached')

    with TraceBlock() as action:
        action.message('Test #2')
        raise TypeError
        print('not reached')
