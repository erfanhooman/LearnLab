"""
the different between repr() and str():
    - repr : string representing the objects as the -developer- want to see (when in terminal we call >>>var that called __repr__ function)
    - str : string representing the objects as the -user- want to see (when we print the var that called __str__ function)

other method for representing:
    - bytes : produce binary representing
"""

"""
    @classmethod set the method to receive the class itself as first argument instead of an instance
    @staticmethod is a function that happens to live in a class body
"""

"""
    the format(<variable>, <format>) show the representing of the format with the wanted format that pass to the 
    format(<variable>, <format>) method on the second argument
"""

from array import array
import math


class Vector2d:
    typecode = 'd'  # <1>

    # if you declare __slots__ you dont have a instance.__dict__ any more and you can control it to save memory
    __slots__ = ('x', 'y')
    # by adding __dict__ in slot you can save memory and have a __dict__ too
    # __slots__ = ("__dict__") : this is useful when you want to use @cached_property
    # __slots__ = ("__weakref__") : this is useful when you want the weak references

    def __init__(self, x, y):
        self.x = float(x)  # <2>
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))  # <3>

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)  # <4>

    def __str__(self):
        return str(tuple(self))  # <5>

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +  # <6>
                bytes(array(self.typecode, self)))  # <7>

    def __eq__(self, other):
        return tuple(self) == tuple(other)  # <8>

    def __abs__(self):
        return math.hypot(self.x, self.y)  # <9>

    def __bool__(self):
        return bool(abs(self))  # <10>

    def __format__(self, fmt_spec=''):
        """this format declare a p for polar coordinate"""
        if fmt_spec.endswith('p'):  # <1>
            fmt_spec = fmt_spec[:-1]  # <2>
            coords = (abs(self), self.angle())  # <3>
            outer_fmt = '<{}, {}>'  # <4>
        else:
            coords = self  # <5>
            outer_fmt = '({}, {})'  # <6>
        components = (format(c, fmt_spec) for c in coords)  # <7>
        return outer_fmt.format(*components)  # <8>


"""
    now we made our Vector2d hashable so it dont change in lifetime and cannot be changed by v1.x = 5
    this way is safer and better
"""


class Vector2d_hashable:
    __match_args__ = ('x', 'y')

    typecode = 'd'

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __hash__(self):
        return hash((self.x, self.y))


...  # the rest of method just like previous version

"""
this method we listed for Vector2d its an usual "Pythonic Objects" for other python programmers to use
"""
