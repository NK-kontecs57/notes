class SuperString:
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return str(self.string)

    def __add__(self, other):
        return SuperString(self.string + other.string)

    def __mul__(self, other):
        return SuperString(self.string * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        return SuperString(self.string[:len(self.string) // other])

    def __lshift__(self, other):
        if other >= len(self.string):
            return SuperString('')
        return SuperString(self.string[:other - 1])

    def __rshift__(self, other):
        if other >= len(self.string):
            return SuperString('')
        return SuperString(self.string[other:])