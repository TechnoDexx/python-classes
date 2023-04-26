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


if __name__ == '__main__':
    import selftest as st
    st.self_test(CardHolder)
