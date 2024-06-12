"""
Type hint in functions
"""
import typing
from typing import List, Optional


def calculate_sum(numbers: Optional[List[int]] = None) -> Optional[int]:
    """
    Calculate the sum of a list of integers.

    Args:
        numbers (Optional[List[int]]): A list of integers. Default is None.

    Returns:
        Optional[int]: The sum of the integers in the list, or None if the list is empty or None.
    """
    if numbers is None:
        return None

    total = sum(numbers)
    return total

"""
** type using on Annotations

* The Any Type (typing.Any) : you can pass objects of every type to an argument of type Any
    -its kinda same as object, but notice that object dont support function like __mul__

    notice that if object support the object, is going to also accept the subclass of that

"""

class T1:
    ...

class T2(T1):
    ...

def f1(p: T1):
    ...


def f2(p: T2):
    ...

o1 = T1
o2 = T2

f1(o2)  # its OK
f2(o1)  # its Not OK


"""
    * Simple Type and Classes : simple like int, str, float, ...
    
    * Optional and Union Type: optional showing that its shortcut for union
        Optional[str] is shortcut for Union[str, None]
        Union[str, bytes] mean str but may bytes
        
        - Union[A, B, Union[C, D] is same as Union[A, B, C, D]
        - Union use full in some type like Union[int, float]
    
    * Generic Collection including tuples and maping :
        - generic collection: list, set, frozenset, ... 
            - write like list[str], set[Any]
        
        - tuple types:
            - tuple as record : tuple[str, floating, str] this is declare record like ('Tehran, 12.32, 'China)
            - tuple as record with named fields: in tuple with many fields or tuple use in many place of code its higly
                recommended to use NamedTuple
            - tuple as immutable sequences : to annotate tuple as unspecified length that are used as immutable lists
                tuple[int, ...]
        
        - generic mapping: in order to show the dict we use 
"""
