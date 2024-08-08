"""
there is a plenty of iterator in itertools and python3

* itertools.count(1, .5) --> 1.0, 1.5, 2.0, ...
* itertools.takewhile(lambda x: x < 1, ..., itertools.count(1, .5)) --> combine this two and stop at 2.5: 1.0, 1.5, 2.0, 2.5
"""
import itertools

""" itertools.compress """
Codes = ['C', 'C++', 'Java', 'Python']
selectors = [False, False, False, True]

Best_Programming = itertools.compress(Codes, selectors)

for language in Best_Programming:
    print(language)  # Output: Python

""" itertools.takewhile """


def is_positive(n):
    return n > 0


value_list = [5, 6, -8, -4, 2]  # drop the value until the first not n > 0 come
result = list(itertools.dropwhile(is_positive, value_list))
print(result)  # Output: [-8, -4, 2]

""" filter(predicate, it) """
result = list(filter(is_positive, value_list))
print(result)  # Output: [5, 6, 2]

""" itertools.filterfalse(predicate, it) : act opposite of the filter """
result = list(itertools.filterfalse(is_positive, value_list))
print(result)  # Output: [-8, -4]

data = 'ABCDEFG'
result = list(itertools.islice(data, 2))  # Start from index 2 (inclusive) # A B

""" itertools.islice() """
itertools.islice(data, 2, 4)  # C D

itertools.islice(data, 1, 4, 2)  # B : 1 to 4 skip 2 - 2

numbers = [1, 2, 3, 4, 5]
accumulated_sums = list(itertools.accumulate(numbers))  # Result: [1, 3, 6, 10, 15]


def multiply(a, b):
    return a * b


accumulated_products = list(itertools.accumulate(numbers, func=multiply))  # Result: [1, 2, 6, 24, 120]

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

doubled_numbers = list(map(lambda x: x * 2, numbers))  # run the function for every number

odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]

numbers = list(itertools.chain(odd, even))  # Output: [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]

strings = ['geeks', 'for', 'geeks']
flattened_strings = list(
    itertools.chain.from_iterable(strings))  # ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']

pairs = [(2, 5), (3, 2), (4, 3)]
result = list(itertools.starmap(pow, pairs))  # Output: [32, 9, 64]

str1 = 'GesoGes'
str2 = 'ekfrek'

combined_values = list(itertools.zip_longest(str1, str2, fillvalue='_'))  # work like zip but consume all of them

A = [1, 2, 3]
B = ['a', 'b']

combined_pairs = list(itertools.product(A, B))  # Output: [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b'), (3, 'a'), (3, 'b')]

dice = range(1, 7)

all_rolls = list(itertools.product(dice, repeat=2))  # Output: [(1, 1), (1, 2), ..., (6, 6)]

a = itertools.count()  # with each next(a) count the next number
b = itertools.cycle('abc')  # with each next(a) cycle the next item

s = 'DPS'
list(itertools.combinations(s, 2))  # [('D', 'P'), ('D', 'S'), ('P', 'S')]
# Combinations are used when only the number of possible groups needs to be found, and the order of arrangements is not important.
list(itertools.combinations_with_replacement(s,
                                             2))  # [('D', 'D'), ('D', 'P'), ('D', 'S'), ('P', 'P'), ('P', 'S'), ('S', 'S')]

numbers2 = [1, 2, 3]
list_permutations = list(itertools.permutations(numbers2, 2))  # Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
# Permutations are used when the order or sequence of arrangement is essential.

# Permutations: Order matters, distinct elements.
# Combinations: Order doesn't matter, similar elements.

""" itertools.groupby """
A = ["apple", "banana", "grape", "kiwi", "orange", "pear", "fig"]

# Sort the data (important for groupby)
A.sort()

for length, group in itertools.groupby(A, key=len):
    print(length, "->", list(group))

#  3: fig, kiwi
#  4: pear, grape
#  5: apple
#  6: orange
#  7: banana

numbers = [1, 2, 3, 4, 5, 6, 7]
iterator1, iterator2 = itertools.tee(numbers, 2)

print(list(iterator1))  # Output: [1, 2, 3, 4, 5, 6, 7]
print(list(iterator2))  # Output: [1, 2, 3, 4, 5, 6, 7]

# The tee() function creates two independent iterators from the same list of numbers


