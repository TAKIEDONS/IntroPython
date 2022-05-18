class magicmethods():
    def __init__(self, name, size):
        self._name = name
        self._size = size

    def __str__(self):
        return f"Magic methods object {self._name} is {self._size}"

    def __repr__(self):
        return f"<magicmethods class (name:{self._name}),(size:{self._size})>"

    def __eq__(self, other):
        return self._name == other._name and self._size == other._size

mm1 = magicmethods("obj1",10)
mm2 = magicmethods("obj2",20)
mm3 = magicmethods("obj1",10)

print(mm1)
print(repr(mm1))

print(mm1==mm2)
print(mm1==mm3)