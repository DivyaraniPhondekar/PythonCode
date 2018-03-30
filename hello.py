class Test:
    def __init__(self):
        self.foo=11
        self._bar=23
        self.__baz=42

t=Test()
print t
print dir(t)
t.foo

