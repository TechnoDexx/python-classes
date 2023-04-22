"""
Выполняет обход дерева наследования снизу вверх, используя ссылки на пространства
имен, и отображает суперклассы с отступами

"""


def class_tree(cls, indent=1):
    print('-' * indent + cls.__name__)
    for supercls in cls.__bases__:
        # print(supercls.__name__)
        class_tree(supercls, indent + 3)


def init_classes():
    global A, B, C, D, E, F

    class A:
        pass

    class B(A):
        pass

    class C(A):
        pass

    class D(B, C):
        pass

    class E:
        pass

    class F(D, E):
        pass


def instance_tree(inst):
    print('Tree of class ', inst)  # inst.__class__.__name__)
    class_tree(inst.__class__, 3)


def self_test():
    instance_tree(A())
    instance_tree(B())
    instance_tree(C())
    instance_tree(D())
    instance_tree(E())
    instance_tree(F())


if __name__ == '__main__':
    init_classes()
    self_test()
