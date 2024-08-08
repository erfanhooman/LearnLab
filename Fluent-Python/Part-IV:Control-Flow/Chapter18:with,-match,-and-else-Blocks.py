import sys


class LookingGlass:

    def __enter__(self):
        self.original_write = sys.stdout.write
        sys.stdout.write = self.reverse_write
        return 'JABBERWOCKY'

    def reverse_write(self, text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_value, traceback):  # this three output is the traceback of error acord in with
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please DO NOT divide by zero!')
            return True


"""
at the start when we call the class using with in the start the LookingGlass __enter__ method will call and at the end
of it we will call the __exit__ method to exit from with statement
"""

with LookingGlass() as what:
    print("alice", "bob")
    print(what)

print("alice", "bob")
print(what)

"""
we can use decorator to implement the Context manager : 
"""
import contextlib


@contextlib.contextmanager
def looking_glass():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write  # before the yield run in __start___
    yield 'JABBERWOCKY'  # the value that bound to the target var in the as clause
    sys.stdout.write = original_write  # after the yield run in __finish__


"""
note that if the error accord in the the body of with the __exit__ never called and left the script in on condition 
status 
"""


@contextlib.contextmanager
def looking_glass():
    original_write = sys.stdout.write

    def reverse_write(text):
        original_write(text[::-1])

    sys.stdout.write = reverse_write
    msg = ''  # <1>
    try:
        yield 'JABBERWOCKY'
    except ZeroDivisionError:  # <2>
        msg = 'Please DO NOT divide by zero!'
    finally:
        sys.stdout.write = original_write  # <3>
        if msg:
            print(msg)


"""
you can use looking glass as decorator beside the with statement :
"""


@looking_glass()
def verse():
    print("test")


verse()  # tset

