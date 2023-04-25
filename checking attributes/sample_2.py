class CardHolder:
    acctlen = 8
    retireage = 56.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.addr = addr

    class Name:
        def __get__(self, instance, owner):
            return self.name

        def __set__(self, instance, value):
            value = value.lower().replace('', '_')
            self.name = value

    name = Name()

    class Age:
        def __get__(self, instance, owner):
            return self.age

        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')
            else:
                self.age = value

    age = Age()

    class Acct:
        def __get__(self, instance, owner):
            return self.acct[:-3] + '***'

        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) != instance.acctlen:
                raise TypeError('invalid acct number!')
            else:
                self.acct = value

    acct = Acct()

    class Remain:
        def __get__(self, instance, owner):
            return instance.retireage - instance.age

        def __set__(self, instance, value):
            raise TypeError('can\'t set remain')

    remain = Remain()


def self_test():
    bob = CardHolder('12345678', 'BobSmith', 40, '123 main st')
    print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
    bob.name = 'Bob Q.Smith'
    bob.age = 50
    bob.acct = '23456789'
    print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
    sue = CardHolder('56781234', 'Sue Jones', 35, '124 main st')
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
