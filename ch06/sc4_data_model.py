""" python data model """

class Vector():
    """ three-dimensional space """
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z


v = Vector(1, 2, 3)
print('v:\n', v)


class Vector(Vector):
    """
    the special method __repr__
    allows the definition of custom string representation
    """
    def __repr__(self):
        return f'Vector({self.x}, {self.y}, {self.z})'


v = Vector(1, 2, 3)
print('v:\n', v)


class Vector(Vector):
    """
    abs() and bool() are two standard python functions
    whose behavior on the Vector class can be defined
    via the special methods __abs__ and __bool__
    """
    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __bool__(self):
        return bool(abs(self))


v = Vector(1, 2, 3)
print('abs(v):\n', abs(v))
print('bool(v):\n', bool(v))

v = Vector()
print('v:\n', v)
print('abs(v):\n', abs(v))
print('bool(v):\n', bool(v))


class Vector(Vector):
    """
    the + and * operators can be applied to almost any python object
    the behavior is defined through the special methods __add__ and __mul__
    """
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Vector(x, y, z)

    def __mul__(self, scalar):
        x = self.x * scalar
        y = self.y * scalar
        z = self.z * scalar
        return Vector(x, y, z)


v = Vector(1, 2, 3)
print('v:\n', v)
print('v + Vector:\n', v + Vector(2, 3, 4))
print('v * 2:\n', v * 2)


class Vector(Vector):
    """
    __len__: len() gives the length of an object in number of elements
    __getitem__: makes indexing via the square bracket notation possible
    """
    def __len__(self):
        return 3

    def __getitem__(self, i):
        if i in [0, -3]:
            item = self.x
        elif i in [1, -2]:
            item = self.y
        elif i in [2, -1]:
            item = self.z
        else:
            raise IndexError('Index out of range.')
        return item


v = Vector(1, 2, 3)
print('v:\n', v)
print('len(v):\n', len(v))
print('v[0]:\n', v[0])
print('v[-2]:\n', v[-2])
try:
    print('v[3]:\n', v[3])
except IndexError as e:
    print('v[3] IndexError:', e)


class Vector(Vector):
    """
    __iter__ defines the behavior during iterations over elements of an object
    an object for which this operation is defined is called iterable
    all collections and containers are iterable
    """
    def __iter__(self):
        for i in range(len(self)):
            yield self[i]


v = Vector(1, 2, 3)

# indirect iteration using index values (via __getitem__)
for i in range(3):
    print(v[i])

# direct iteration over the class instance (via __iter__)
for coordinate in v:
    print(coordinate)
