class ResultSet(object):
    def __init__(self, table=None, root=None, precision=None, time=None, iters=None, equations=[], hLines=[],
                 vLines=[]):
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
        return self.numIters

    def __str__(self):
        string = "Equation: " + str(self.equations[0]) + "\n"
        string += "Root: " + str(self.root) + "\n"
        string += "Number of Iterations: " + str(self.numIters) + "\n"
        string += "Precision: " + str(self.precision) + "\n"
        string += "Execution Time: " + str(self.time) + "\n"
        string += "Vertical Boundary Lines: " + str(self.vLines) + "\n"
        string += "Horizontal Boundary Lines: " + str(self.hLines) + "\n"
        if len(self.equations) > 1:
            string += "Other boundary equations: " + str(self.equations[1:]) + "\n"
        string += "Table:\n"
        string += str(self.table)
        return string
