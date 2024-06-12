"""
before we write a code using the abstract based, this type of programing called Strategy Design Patterns
    'refer to example in page 344-345 of book'

in the strategy design patterns we have strategy for a different model for example we have three type of discounting
in shop so we make different strategy for each type of discount
"""

"""
- Strategy Pattern: 

globals() function return a dict representing the current global symbol table
from decimal import Decimal
from strategy import Order
from strategy import (
    A_strategy, B_strategy, C_strategy
)
strategy = [strategy for name, strategy in globals.items()
            if name.endswith('_strategy') and
                 name != 'best_promo'] # avoid an infinite recursion
            )

def best_promo(order: Order):
    return max(promo(order) for promo in promos)
    
this line of code suggest that we can work with function as first-class

- Decorator Enhanced Strategy Pattern:
another way to add permission is using the decorated:

    # this decorator get the function, add to the promos list and then return function unchanged
    def promotion(promo: Promotion): 
        promos.append(promo)
        return promo
    
    @promotion
    def A_strategy(order: Order):
        ...
        
    @promotion
    def B_strategy(order: Order):
        ...
    
    @promotion
    def C_strategy(order: Order):
        ...
        
 
decorator its better than using the globals() because 
    1. decorator can be easily commented and dont add to the list another
    2. no need to naming like _strategy at the end of the strategy named
"""

