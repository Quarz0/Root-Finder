class Table(object):
    def __init__(self, title, header, data):
        assert type(header) == type([]) and type(data) == type([])
        for row in data:
            assert type(row) == type([]) and len(row) == len(header)

        self.header = header
        self.data = data
        self.title = title

    def getTitle(self):
        return self.title

    def getHeader(self):
        return self.header

    def getData(self):
        return self.data

    def getTable(self):
        return self.header + self.data

    def __str__(self):
        string = "Table Title: " + str(self.title) + "\n" + str(self.header) + "\n"
        for row in self.data:
            string += str(row) + "\n"
        return string
