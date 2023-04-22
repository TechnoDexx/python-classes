"""
Attribute
"""


class Empty:

    def __getattr__(self, attrname):
        """
        Get Attribute
        :param attrname:
        :type attrname:
        :return:
        :rtype:
        """
        if attrname == 'age':
            return 45
        else:
            raise AttributeError(attrname)


class AccessControl:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value
        else:
            raise AttributeError(attr + ' not allowed')


if __name__ == '__main__':
    # X = Empty()
    # print(X.age)
    # print(X.name)
    # print()
    X = AccessControl()
    X.age = 50
    X.name = 'mel'
    print(X.age)
