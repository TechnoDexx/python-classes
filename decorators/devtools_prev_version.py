def rangetest(*argchecks):
    def OnDecorator(func):
        if not __debug__:
            return func
        else:
            def OnCall(*args):
                for (ix, low, high) in argchecks:
                    if args[ix] < low or args[ix] > high:
                        errmsg = 'Argument {0} not in {1}...{2}'.format(ix, low, high)
                        raise TypeError(errmsg)
                return func(*args)

            return OnCall

    return OnDecorator
