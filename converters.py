from streams import Processor


class UpperCase(Processor):
    def converter(self, data):
        return data.upper()


class Plize:
    def write(self, data):
        print('<p>{0}</p>'.format(data.rstrip()))


class HTMLize:

    def write(self, data):
        print('<PRE>{0}</PRE>'.format(data.rstrip()))


if __name__ == '__main__':
    import sys

    obj = UpperCase(open('spam.txt'), sys.stdout)
    obj.process()
    UpperCase(open('spam.txt'), HTMLize()).process()
    UpperCase(open('spam.txt'), Plize()).process()
    obj = UpperCase(open('spam.txt'), open('spam_up.txt', 'w'))
    obj.process()
