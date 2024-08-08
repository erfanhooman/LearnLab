"""
Implement a Simple Decorator
"""
import functools
import time


def timer_decorator(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)  # this line only works because the closure make the func free variable
        t1 = time.perf_counter() - t0
        print(f"time to run {func.__name__}: {t1}")
        return result
    return inner


@timer_decorator
def snooze(sec):
    time.sleep(sec)


"""
the output of snooze(2.5) is like
    $ time to run snooze: 2.500124986996525

remember this code actually does this :
    snooze = timer_decorator(snooze)

note if i dont use the @functools.wraps(func) decorator outside the functions if i print the snooze.__name__
    it will print the name of the "timer_decorator" (also for other metadata) to avoid this happening we use 
    @functools.wraps(func) decorator
"""

"""
-another decorator functools.cache it will use to cache the function so it didnt compute function every time
-This can significantly speed up your program if the function is computationally expensive and is called multiple 
times with the same arguments
-it use in the recursive function quite often
"""


@functools.cache
@timer_decorator  # Stacked decorator its like this factorial = functools.cache(timer_decorator(factorial))
def factorial(n):
    return n * factorial(n - 1) if n else 1  # in the recursive the decorator will run each time the function called


print(factorial(10))  # no previously cached result, makes 11 recursive calls
print(factorial(5))  # just looks up cached value result
print(factorial(12))  # makes two new recursive calls, the other 10 are cached
