"""
we have 4 way to define a interface:
    1.duck typing
    2.goose typing
    3.static typing
    4.static duck typing

there are two type of protocols in python:
    1. Dynamic Protocol: an object may implement only part of a dynamic protocol and still be useful
    2. static Protocol: to fulfill a static protocol, the object must provide every method declared in the protocol class

    the example of the Dynamic Protocol is that when you implement __getitem__ and __len__ python will handle other
        method in Sequence such as __iter__ and __contain__ (for 'in' keyword)

    because of the duck typing in python its better not to use isinstance or type(foo) is bar
    instead suggest to use something like this:
"""
import collections.abc

field_names = input()
try:
    field_names = field_names.replace(',', ' ').split()  # extract the iterable item
except AttributeError:  # sorry the field_names don't quack like a str and dont have a split() method
    pass  # so it's already an iterable item

for x in field_names:
    print(x, "-")

from collections.abc import MutableSequence


class MyList(MutableSequence):
    """
    The MutableSequence class inherits from collections.abc.Sequence, which itself inherits from collections.abc.Sized
    and collections.abc.Iterable. This means that any class that inherits from MutableSequence must implement the methods
    specified by these base classes, such as __getitem__, __len__, and __iter__.

    The primary use of abc.MutableSequence is to define the interface for mutable sequences and enforce the implementation
    of necessary methods. By subclassing MutableSequence and implementing the required methods, you can create custom
    mutable sequence types that can be used interchangeably with built-in mutable sequences like lists.
    """

    def __init__(self, data=None):
        self._data = list(data) if data else []

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def __len__(self):
        return len(self._data)

    def insert(self, index, value):
        self._data.insert(index, value)

    def __str__(self):
        return str(self._data)


"""
_ Writing Code in the ABC way:
   its content the concrete methods and abstract methods (interfaces)
    note: the concrete nmethods must rely on the abstract methods (interfaces)
"""