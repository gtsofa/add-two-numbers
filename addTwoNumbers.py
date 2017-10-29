class Addition(object):
    def addNumbers(self, a, b):
        number_types = (int, float, complex)

        if isinstance(a, number_types) and isinstance(b, number_types):
            return a + b
        else:
            raise ValueError
