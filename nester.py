def generate():
    class Spam:
        count = 1

        def method(self):
            print(Spam.count)
    return Spam()


if __name__ == '__main__':
    generate().method()
    print(Spam.count)
