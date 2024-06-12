"""
10.py:
    Write a program that receives a sequence of numbers separated by commas and puts them in a list and a tuple.
"""


def sequence_to_list_tuple():
    sequence = input("Enter a sequence of numbers separated by commas: ")

    sequence_list = [int(a) for a in sequence.split(",")]
    sequence_tuple = (int(a) for a in sequence.split(","))

    return sequence_list, sequence_tuple


if __name__ == "__main__":
    sequence_list, sequence_tuple = sequence_to_list_tuple()
    print("List:", sequence_list)
    print("Tuple:", type(sequence_tuple))
