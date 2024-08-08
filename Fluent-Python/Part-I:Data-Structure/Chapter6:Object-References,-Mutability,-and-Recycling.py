"""
    the 'is' show if both var have the same id and reference of one var
    the == show if the value of the both is same
"""

l1 = [1, 2, 3]
l2 = l1
print(l2 is l1)  # True

l3 = list(l2)

print(l3)  # [1, 2, 3]

print(l2 is l3)  # False

"""
    Shallow Copy and Deep Copy
"""


class Bus:
    def __init__(self, passengers: list):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)


import copy

bus1 = Bus(['Alice', 'Bill', 'Clarie', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)

print(id(bus1), id(bus2), id(bus3))
# 139704457496464, 139704457496528, 139704460637200

bus1.drop('Bill')
print(bus1.passengers)  # ['Alice', 'Clarie', 'David']
print(bus2.passengers)  # ['Alice', 'Clarie', 'David'] : changing the bus 1 , effect on the bus 2 too

''' changing the bus 1 , dont effect on the bus 3 cause its deep copy '''
print(bus3.passengers)  # ['Alice', 'Bill', 'Clarie', 'David']

'''
Note: copy is shallow by default
Note: You can control the behaviour of copy and deep copy buy implementing __copy__() and __deepcopy__()
Note: the shallow copy change the value of mutable item(list, object like a bus we made, etc) when you make the change in the copy, 

Note: the parameter passing act like making shallow copy
'''

'''
using the mutable type as parameter defaults is bad idea
when work with the mutable item in class better work like below
'''


class HuntedBus:
    def __init__(self, passengers: list = None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)


'''
****
    how del keyword: 
        delete the reference to object 
            Garbage collector wait and delete the object when all of the reference deleted
'''
