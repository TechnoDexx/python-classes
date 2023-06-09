class Super:

    def method(self):
        print('In Super.method')

    def delegate(self):
        self.action()

    def action(self):
        raise NotImplementedError('Action must be defined!')


class Inheritor(Super):
    pass


class Replacer(Super):
    def method(self):
        print('In Replacer.method')


class Extender(Super):
    def method(self):
        print('Starting Extender.method')
        Super.method(self)
        print('Ending Extender.method')


class Provider(Super):
    def action(self):
        print('In Provider.action')


if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n {} ...'.format(klass.__name__))
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()

