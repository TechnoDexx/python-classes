# Простая фуекция также может играть роль метакласса
def MetaFunc(classname, supers, classdict):
    print('In MetaFunc: ', classname, supers, classdict)
    return type(classname, supers, classdict)


class Eggs:
    pass


print('Making Class...')


class Spam(Eggs, metaclass=MetaFunc):
    data = 1

    def meth(self, args):
        pass


print('Making Instance...')

X = Spam()

print('data: ', X.data)