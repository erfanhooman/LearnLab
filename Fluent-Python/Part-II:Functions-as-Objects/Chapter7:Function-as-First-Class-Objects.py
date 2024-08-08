"""
**  the function in python is first class mean you can work with it like var, pass it to function, return it from function
    other of example of the first class is str, int, etc

**  Higher_order a function is the function that get the function as input or return a function
"""
# example of writing higher-order function :

def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        return sum(series) / len(series)

    return averager()

avg = make_averager()
avg(10) # now we can assign any value to be a function


import random
class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    # using the __call__() method in class you can make the class callable
    def __call__(self):
        return self.pick()


bingo = BingoCage(range(3))
bingo.pick()
# is same as
bingo()


"""
**  sorted built in function is higher order function
    we need to pass the function as key= input
    
    sometimes we want to say that sort the list of tuple, using the third item in each tuple
    print(result)  # Output: 8
    List = [('Ali', 'Ahmadi', 'Tehran'),
        ('John', 'Smith', 'London'), 
        ('Saber', 'Abadi', 'Paris')]
        
    we can't pass the list[2] as the key= in the sorted() function because the key= give the function as input 
    so we use operator.attrgetter() function  
"""

from operator import attrgetter
metro_areas = ... # the list of namedtuple
for city in sorted(metro_areas, key=attrgetter('coord.lat')) # sort by the lat of the coord
    print(city)

"""
same as previous problem, when we need to use method and pass it as function we use method operator.caller()
"""

from operator import methodcaller
s = 'test string'
upcase = methodcaller('upper')
print(upcase(s)) # same result as s.upper

"""
** functools module
    
    before we have reduce from this functools
"""

from functools import reduce

# Example 1: Summing up a list of numbers
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)  # Output: 15

"""
map(): is used to apply a function to each element of an iterable and returns an iterable, 

reduce(): is used to apply a rolling computation to sequential pairs of values in a sequence, ultimately reducing them 
to a single value.

filter(): applies a function to each element of an iterable and returns only those elements for which the function
returns True.
"""
# map
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))  # Output: [2, 4, 6, 8, 10]

# reduce
from functools import reduce
# Summing up a list of numbers
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)  # Output: 15

"""
** another function of the functools.partial
    we use when we want to wait and enter the second argument another time
"""

from functools import partial

# Define a simple function
def power(base, exponent):
    return base ** exponent

# Create a partial function with base=2
square = partial(power, 2)

# Call the partial function with only the exponent
result = square(3)  # Equivalent to calling power(2, 3)