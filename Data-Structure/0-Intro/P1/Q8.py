"""
8.py:
    Write a program that receives a Python string with an odd length and greater than seven from the user and the middle string
    print it with a length of three
"""


def string_slicing(__str):
    length = len(__str)
    if length % 2 == 0 or length < 7:
        raise ValueError

    middle = length // 2
    middle_part = __str[middle - 1 : middle + 2]
    print(middle_part)


if __name__ == "__main__":
    try:
        # string_input = input("Enter a string : ")
        string_slicing("123456789")
    except ValueError:
        print("Invalid Input : please enter string with an odd length and greater than seven")