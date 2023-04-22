class Processor:
    def __init__(self, reader, writer):
        self.reader = reader
        self.writer = writer

    def process(self):
        while 1:
            data = self.reader.readline()
            if not data:
                break
            data = self.converter(data)
            self.writer.write(data)
        # self.writer.close()

    def converter(self, data):
        raise NotImplementedError('converter must be defined!')
