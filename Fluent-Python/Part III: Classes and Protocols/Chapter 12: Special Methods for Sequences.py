import functools
import operator

class MyCustomList:
    """
    declare the __getattr__ so it also support slicing
    """
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        if isinstance(index, slice):
            # If index is a slice object
            return self.data[index.start:index.stop:index.step]
        else:
            # If index is an integer or something else
            return self.data[index]


class MyClass:
    def __init__(self, values):
        self.values = values

    def __setattr__(self, name, value):
        print(f"Setting attribute {name} to {value}")
        super().__setattr__(name, value)

    def __hash__(self):
        # Use functools.reduce and operator.xor to combine hash values
        return functools.reduce(operator.xor, map(hash, self.values))

obj1 = MyClass((1, 2, 3))
obj2 = MyClass((1, 2, 3))

"""
zip() functions
"""

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y', 'z']

zipped = zip(list1, list2, list3)

for item in zipped:
    print(item)

"""
The Implementing of the Vector of N with required vector
"""

from array import array
import reprlib
import math
import functools
import operator
import itertools  # <1>


class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return f'Vector({components})'

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components))

    def __eq__(self, other):
        return (len(self) == len(other) and
                all(a == b for a, b in zip(self, other)))

    def __hash__(self):
        hashes = (hash(x) for x in self)
        return functools.reduce(operator.xor, hashes, 0)

    def __abs__(self):
        return math.hypot(*self)

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, key):
        if isinstance(key, slice):
            cls = type(self)
            return cls(self._components[key])
        index = operator.index(key)
        return self._components[index]

    __match_args__ = ('x', 'y', 'z', 't')

    def __getattr__(self, name):
        cls = type(self)
        try:
            pos = cls.__match_args__.index(name)
        except ValueError:
            pos = -1
        if 0 <= pos < len(self._components):
            return self._components[pos]
        msg = f'{cls.__name__!r} object has no attribute {name!r}'
        raise AttributeError(msg)

    def angle(self, n):  # <2>
        r = math.hypot(*self[n:])
        a = math.atan2(r, self[n-1])
        if (n == len(self) - 1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self):  # <3>
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, fmt_spec=''):
        if fmt_spec.endswith('h'):  # hyperspherical coordinates
            fmt_spec = fmt_spec[:-1]
            coords = itertools.chain([abs(self)],
                                     self.angles())  # <4>
            outer_fmt = '<{}>'  # <5>
        else:
            coords = self
            outer_fmt = '({})'  # <6>
        components = (format(c, fmt_spec) for c in coords)  # <7>
        return outer_fmt.format(', '.join(components))  # <8>

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)