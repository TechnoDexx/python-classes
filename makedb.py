from person import Person, Manager
import shelve


def save_data():
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job="dev", pay=100000)
    tom = Manager('Tom Jones', 50000)
    with shelve.open('persondb.dat') as db:
        for obj in (bob, sue, tom):
            db[obj.name] = obj

    print('Data saving complete')


def load_data():
    with shelve.open('persondb.dat') as db:
        print('Database Length: {0}'.format(len(db)))
        print('Database Keys: {0}'.format(list(db.keys())))
        bob = db['Bob Smith']
        print(bob)
        print('{0} LastName: {1}'.format(bob.name, bob.lastName()))
        for key in db:
            print('{0} => {1}'.format(key, db[key]))
        print('\nSorted: ')
        for key in sorted(db):
            print('{0} => {1}'.format(key, db[key]))


if __name__ == '__main__':
    save_data()
    load_data()
