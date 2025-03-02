"""
2.py :
    Write a program in Python language that receives a string from the user and prints its reverse (without use
    from the function reverse)
"""


def reverse_string(__str):
    reversed_string = ""

    for char in __str:
        reversed_string = char + reversed_string

    return reversed_string


if __name__ == "__main__":
    str_input = input("Enter a string : ")
    print(reverse_string(str_input))