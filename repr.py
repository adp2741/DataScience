
class OpaqueClass(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


obj = OpaqueClass(1, 2)
print(obj)


class OpaqueClassRepr(OpaqueClass):
    def __init__(self, x, y):
        super().__init__(x, y)

    def __repr__(self):
        return f"OpaqueClass({self.x}, {self.y})"


obj2 = OpaqueClassRepr(3, 4)
print(obj2)
