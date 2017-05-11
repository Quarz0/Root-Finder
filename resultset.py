class ResultSet(object):
    def __init__(self, table=None, root=None, precision=None, time=None, iters=None, equations=[], boundaries=[]):
        self.table = table
        self.root = root
        self.precision = precision
        self.time = time
        self.numIters = iters
        self.equations = equations
        self.boundaries = boundaries

    def getBoundaries(self):
        return self.boundaries

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

    def __str__(self):
        string = "Root: " + str(self.root) + "\n"
        string += "Number of Iterations: " + str(self.numIters) + "\n"
        string += "Precision: " + str(self.precision) + "\n"
        string += "Execution Time: " + str(self.time) + "\n"
        string += "Table:\n"
        string += str(self.table)
        return string
