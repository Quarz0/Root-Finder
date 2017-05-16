class equation(object):
    def __init__(self, eqn, is_vertical=False, is_horizontal=False):
        if is_vertical:
            self.is_vertical = True
            self.is_horizontal = False
        elif is_horizontal or len(list(eqn.free_symbols)) == 0:
            self.is_vertical = False
            self.is_horizontal = True
        else:
            self.is_vertical = False
            self.is_horizontal = False
        self.eqn = eqn

    def get_eqn(self):
        return self.eqn

    def is_vertical(self):
        return self.is_vertical

    def __str__(self):
        return str(self.eqn)
