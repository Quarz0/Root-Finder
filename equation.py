class equation(object):
    def __init__(self, eqn, is_vertical=False):
        if is_vertical:
            self.is_vertical = True
        else:
            self.is_vertical = False
        self.eqn = eqn

    def get_eqn(self):
        return self.eqn

    def is_vertical(self):
        return self.is_vertical

    def __str__(self):
        return str(self.eqn)
