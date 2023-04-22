import shelve
with shelve.open('persondb.dat') as db:
    sue = db['Sue Jones']
    sue.giveRaise(.10)
    db['Sue Jones'] = sue

    for key in sorted(db):
        print('{0} => {1}'.format(key, db[key]))

