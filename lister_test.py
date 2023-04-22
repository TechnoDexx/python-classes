from lister import ListInstance


class Spam(ListInstance):
    def __init__(self):
        self.data1 = "food"
        self.data2 = "krank"
        self.data3 = 1977


if __name__ == '__main__':
    x = Spam()
    print(x)
