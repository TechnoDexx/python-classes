"""
Файл devtools.py: декоратор функций, выполняющий проверку аргументов на
вхождение в заданный диапазон. Проверяемые аргументы передаются декоратору в
виде именованных аргументов. В фактическом вызове функции аргументы могут
передаваться как в виде позиционных, так и в виде именованных аргументов,
при этом аргументы со значениями по умолчанию могут быть опущены.
Примеры использования приводятся в файле devtools_test.py.
"""
trace = True


def rangetest(**argchecks):
    def OnDecorator(func):
        if not __debug__:
            return func
        else:
            import sys
            code = func.__code__
            allargs = code.co_varnames[:code.co_argcount]
            funcname = func.__name__

            def OnCall(*pargs, **kargs):
                # Все аргументы в кортеже pargs сопоставляются с первыми N
                # ожидаемыми аргументами по позиции
                # Остальные либо находятся в словаре kargs, либо опущены, как
                # аргументы со значениями по умолчанию
                positionals = list(allargs)
                positionals = positionals[:len(pargs)]
                for (argname, (low, high)) in argchecks.items():
                    # Для всех аргументов, которые должны быть проверены
                    if argname in kargs:
                        # Аргумент был передан по имени
                        if kargs[argname] < low or kargs[argname] > high:
                            errmsg = '{0}: argument "{1}" not in {2}...{3}'
                            errmsg = errmsg.format(funcname, argname, low, high)
                            raise TypeError(errmsg)
                    elif argname in positionals:
                        # Аругмент был передан по позиции
                        position = positionals.index(argname)
                        if pargs[position] < low or pargs[position] > high:
                            errmsg = '{0}: argument "{1}" not in {2}..{3}'
                            errmsg = errmsg.format(funcname, argname,
                                                   low, high)
                            raise TypeError(errmsg)
                    else:
                        # Аргумент не был передан: предполагается, что он
                        # имеет значение по умолчанию
                        if trace:
                            print('Argument "{0}" defaulted'. format(argname))
                return func(*pargs, **kargs)
            return OnCall
    return OnDecorator

