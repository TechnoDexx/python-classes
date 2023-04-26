def self_test(pClass):
    if pClass.__name__ == 'CardHolder':
        bob = pClass('12345678', 'BobSmith', 40, '123 main st')
        print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
        bob.name = 'Bob Q.Smith'
        bob.age = 50
        bob.acct = '23456789'
        print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
        sue = pClass('56781234', 'Sue Jones', 35, '124 main st')
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
    elif pClass.__name__ == '':
        pass
