class A:
    def __mul__(self, other, unexpected):  # Noncompliant. Too many parameters
        return 42

    def __add__(self):  # Noncompliant. Missing one parameter
        return 42
