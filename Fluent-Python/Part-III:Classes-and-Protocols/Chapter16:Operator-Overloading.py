"""
You can do the Operator Overloading in python class using the magic methods
"""

"""
in adding a + b first check the __add__ of the method a, if it dosen't have a __add__ check the __radd__ method of b

but note in order that after checking the __add__ the interpreter go on the __radd__ of the b should __add__ methods 
return NotImplemented, so its good practice to catch the TypeError and return the NotImplemented
"""

"""
infix operators:

+   : __add__, __radd__, __iadd__
-   : __sub__, __rsub__, __isub__
*   : __mul__, __rmul__, __imul__

/   : __truediv__, __rtruediv__, __itruediv__
//  : __floordiv__, __rfloordiv__, __ifloordiv__
%   : __mod__,      __rmod__,      __imod

**  : __pow__, __rpow__, __ipow__
@   : __matmul__, __rmatmul__, __imatmul__
&   : __and__, __rand__, __iand__
|   : __or__, __ror__, __ior__
^   : __xor__, __rxor__, __ixor__

<<   : __lshift__, __rlshift__, __ilshift__
>>   : __rshift__, __rrshift__, __irshift__

"""

"""
In Comparison there is no __r__ method if the method missing(or return NotImplemented its going to check the method 
in the b if its still missing(or return NotImplemented) too then its compare there IDs

== : __eq__,  != : __ne__,  > : __gt__,  < : __lt__,  >= : __ge__,  <= : __le__

most of time you don't need to implement __ne__ for != because the fallback behavior of __ne__, when __eq__ is defined
and does not return the NotImplemented, __ne__ return the result negated
"""

"""
if we don't implement the __i**__ its going to work fine and do the job according to the __**__ method but the problem 
is that when you see the id, its going to create a new object with new id to store the answer if you want to store in 
the same object with same id of the before (like a original behavior of the i**, you have to use the __i**__
"""

