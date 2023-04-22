def kaboom(x, y):
    return x + y


try:
    kaboom([0, 1, 2], 'spam')
except TypeError:
    print('Hello, World!')
print('Resuming here')
