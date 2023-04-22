from spam import Spam
# TODO
print('Create three instances of the Spam() object')
a = Spam()
b = Spam()
c = Spam()
print('Done')
print()
print(Spam.printNumInstances())
print()
print('Delete first instance')
del a
print('Done')
print()
print(Spam.printNumInstances())
print()
print('Delete all other instances')
del b, c
print('Done')
print()
print(Spam.printNumInstances())
print()
