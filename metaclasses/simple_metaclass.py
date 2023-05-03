"""
В действительности этот метакласс ничего не делает (с тем же успехом мы
могли бы позволить создать класс с помощью класса по умолчанию type), но
он демонстрирует способ, каким можно задействовать метакласс в процедуре
создания класса для его расширения.
"""


class Meta(type):
    def __new__(cls, classname, superclasses, attributedict):
        return type.__new__(cls, classname, superclasses, attributedict)
