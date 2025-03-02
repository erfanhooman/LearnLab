"""
9.py:
    Receive two lists from the user and in a function, print a list that contains the values in the odd indices of the list
    first and the values of the even indices of the second list.
"""


def list_odd_even(list1, list2):

    result = [a for a in (list1[1::2] + list2[::2])]
    print(result)


if __name__ == "__main__":
    try:
        list1 = input("Enter the list 1 (comma-separated values): ").split(",")
        list2 = input("Enter the list 2 (comma-separated values): ").split(",")

        list_odd_even(list1, list2)

    except ValueError:
        print("Invalid input")