class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.__acct = acct
        self.__name = name
        self.__age = age
        self.addr = addr

    def getName(self):
        return self.__name

    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value

    name = property(getName, setName)

    def getAge(self):
        return self.__age

    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('Invalid age')
        else:
            self.__age = value

    age = property(getAge, setAge)

    def getAcct(self):
        return self.__acct[:-3] + '***'

    def setAcct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invalid account number!')
        else:
            self.__acct = value

    acct = property(getAcct, setAcct)

    def remainGet(self):
        return self.retireage - self.__age

    remain = property(remainGet)
def self_test():
    bob = CardHolder('1234 - 5678', 'BobSmith', 40, '123 main st')
    print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
    bob.name = 'Bob Q.Smith'
    bob.age = 50
    bob.acct = '23456789'
    print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
    sue = CardHolder('5678 - 12 - 34', 'Sue Jones', 35, '124 main st')
    print(sue.acct, sue.name, sue.age, sue.remain, sue.addr, sep=' / ')
    try:
        sue.age = 200
    except:
        print('Bad age for Sue')
    try:
        sue.remain = 5
    except:
        print("Can't set sue.remain")
    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for Sue')


if __name__ == '__main__':
    self_test()