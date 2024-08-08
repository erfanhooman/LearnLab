""" Data Class Builder """
import typing

''' *---- Collection Named Tuple ----* '''

from collections import namedtuple

City = namedtuple('City', 'name country population coordinate')

tokyo = City(name="Tokyo", country="Japan", population=37000, coordinate=(35, 139))

# print(tokyo.name, tokyo.country, tokyo.country)

# print(City._fields)

tehran_data = ("Tehran", "Iran", 85000, (12, 45))

tehran = City._make(tehran_data)

# Convert to Dict
import json

tehran_dict = tehran._asdict()

json.dumps(tehran_dict)

''' *---- Typed Named Tuple ----* '''

from typing import NamedTuple, ClassVar


class City2(NamedTuple):
    name: str
    population: int
    coordinate: tuple


# *Notice this are just the hint and there is no type checking at the runtime
# *You can initialize a variable with type and default like this
variable_name: str = "default value for the variable"
# *Again notice this are just the hint and there is no type checking at the runtime


paris = City2(name="paris", population=36000, coordinate=(35, 39))

''' *---- @dataclass ----* '''

from dataclasses import dataclass, field


# different between dataclass and typing namedtuple is on page 176-177 of fluent python
@dataclass
class City3:
    name: str
    population: int = 20000
    # states: list = [] //Err : you can initialize an empty list like this u should use following line
    states: list = field(default_factory=list)  # []
    # this is why each instance going to own list and all of them don't use the same list


# __post_init__ is for dataclass and called after the value is initialize
# I also declare the set for all of the city name that can be access by all instance
@dataclass
class City4:
    all_name: ClassVar[
        set[str]] = set()  # this is the set of all the name and we add each name in every instance we made
    name: str
    country: str

    def __post_init__(self):
        self.name_country = f"{self.country}: {self.name}"
        self.all_name.add(self.name)
        # print(self.all_name,"---")

    # to represent the data class when print the instance
    def __repr__(self):
        return "represent"


# The Danger in the match-case :
'''
match x:
    case float: # in this case python see float as var and match any subject
        do_smt_with(x)  
        
match x:
    case float():
        do_smt_with(x)
        
'''


# Pattern Matching in Data Classes
class City5(typing.NamedTuple):
    continent: str
    name: str
    country: str


cities = [
    City5('Asia', 'Tokyo', 'JP'),
    City5('Asia', 'Delhi', 'IN'),
    City5('North America', 'Mexico City', 'MX'),
    City5('North America', 'New York', 'US'),
    City5('South America', 'Sao Paulo', 'BR')
]

for city in cities:
    results = []
    match city:
        case City5(continent='Asia', country=cc):
            results.append(cc)

        # we can also do this like this
        case City5('Asia', _, cc):
            results.append(cc)

        # the argument we can match: (City5.__match_args__):
        # > ('continent', 'name', 'country')
