"""
Decorators in python for modify a function in python
"""
import functools
import time


def deco(func):
    def inner():
        print("inner function running")

    return inner


@deco
def target():
    print("target function running")


target()  # it will print the "target function running"

"""
Notice that they run right after the decorated function is defined
"""


# registration.py
def deco2(func):
    def inner2():
        print(f"inner 2 function running for {func}")

    return inner2


@deco2
def f1():
    print("f1 running")


@deco2
def f2():
    print('f2 running')


print("run before functions")
f1()
f2()

# the output be like this :

# $ inner 2 function running for <function f1 at 0x7f165c20eb60>
# $ inner 2 function running for <function f2 at 0x7f165c20eca0>
# run before functions
# $ f1 running
# $ f2 running

"""
so when you import registration.py it will run the decorators first
"""

"""
before we start to know Closure first better to review 'Variable scope Rules':

- we know that the code below is on error in b

b = 6
def f(a):
    print(a)
    print(b) # this code have error

and you should write it like this :  
"""

b = 6


def f(a):
    global b
    print(a)
    print(b)


"""
Closures:
    look at the example below 
    the series list in the make_averager() function update every time and local scope is long-gone after avg(10)
    is called 
    this concept named closure
"""


def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)
        return sum(series) / len(series)

    return averager


avg = make_averager()
avg(10)

"""
if we write a function like below we find the problem according because of the 'Variable scope Rules'

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        count += 1
        total += new_value
        return count / total

    return averager
    
we can't do this because this item are immutable, but its ok with mutable item such as lists
to fix this problem we can use the nonlocal keyword
"""


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return count / total

    return averager


"""
nonlocal vs global keyword:
    - 'nonlocal' lets you declare a variable as a free variable even when it is assigned within the function
        the nonlocal variable is used in nested function to access and modify variables from a non-global scope.
        
    - The global keyword is used to access and modify variables in the global scope, which is outside any function.
"""

"""
Parameterized Decorators
"""


def split_number(num):
    def decorator(func):
        def inner(*args, **kwargs):
            res = func(*args, **kwargs)
            return res / num

        return inner

    return decorator


@split_number(3)
def add(a, b):
    return a + b

