import manynames

X = 66
print(X)                # 66: здешняя глобальная переменная
print(manynames.X)      # 11: глобальная, ставшая атрибутом в результате импорта
manynames.f()           # 11: X в manynames, не здешняя глобальная!
manynames.g()           # 22: локальная в функции, в другом файле

print(manynames.C.X)    # 33: атрибут класса в другом модуле
I = manynames.C()
print(I.X)              # 33: все еще атрибут класса
I.m()
print(I.X)              # 55: а теперь атрибут экземпляра!
