class Table(object):
    def __init__(self, header, data):
        assert type(header) == type([]) and type(data) == type([])
        for row in data:
            assert type(row) == type([]) and len(row) == len(header)

        self.header = header
        self.data = data

    def getHeader(self):
        return self.header
    def getData(self):
        return self.data
    def getTable(self):
        return self.header + self.data
