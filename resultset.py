class ResultSet(object):
    def __init__(self, table = None, root = None, precision = None, time = None, iters = None, equations = [], hLines = [], vLines = []):
        self.table = table
        self.root = root
        self.precision = precision
        self.time = time
        self.numIters = iters
        self.equations = equations
        self.hLines = hLines
        self.vLines = vLines

    def getHLines(self):
        return self.hLines
    def getVLines(self):
        return self.vLines
    def getEquations(self):
        return self.equations
    def getTable(self):
        return self.table
    def getRoot(self):
        return self.root
    def getPrecision(self):
        return self.precision
    def getExecutionTime(self):
        return self.time
    def getNumberOfIterations(self):
        return self.NumIters
