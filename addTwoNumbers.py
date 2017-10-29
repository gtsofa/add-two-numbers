class Addition(object):
    def addNumbers(self, a, b):
        number_types = (int, float, complex)

        if isinstance(a, number_types) and isinstance(b, number_types):
            import pdb; pdb.set_trace()
            return a + b
        else:
            raise ValueError("Check, either both or one of your arguments is not a number")
