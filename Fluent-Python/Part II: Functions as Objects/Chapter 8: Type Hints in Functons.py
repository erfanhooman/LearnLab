"""
we use the Numpy for type checking, this type of the programing known as 'Gradual Typing'
"""
"""
you can use tools like flake8 and blue.flake8
"""

"""
- for set default in type hints you can easily use = but when we want to use a None as Default must choose the
    typing.Optional[str] saying the variable can be str or None
    
- sometime we can have any of the str, 
"""

"""
Type usable in Annotations:
    - typing.Any: its accept anything 
        like the type object( the problem is the object don't support __mul__ operation
        
    - Simple Types and Classes: simple type like int, float, str, bytes
    
    -Optional and Union Types: typing.Optional[str] is shortcut for Union[str, None]
        Union[a, b, c] says that the type can be a or b or c
        
    -Generic Collections: Generic collections allow you to specify the type of elements that a collection can hold.
        list: List[int]
        Tuples can have elements of different types. You can specify the types of elements in a tuple using the Tuple 
        type from the typing module, 
            A tuple with fixed types (Tuple as record): Tuple[str, int]
            A tuple with variable length but same type for all elements(Tuple[int, ...])
        Generic Mappings(like dictionaries): Dict[KeyType, ValueType]
            in general it's better to use abc.Mapping or abc.MutableMapping instead of dict
            
    - 
"""