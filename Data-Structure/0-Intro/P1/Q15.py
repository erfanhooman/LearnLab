"""
15.py:
    Write a function that receives a variable number of arguments as input and calculates and returns the total and maximum value of the arguments.
"""


def calculate_total_and_max(*args):
    total = sum(args)
    maximum = max(args)
    return total, maximum


if __name__ == "__main__":
    total, max = calculate_total_and_max(5, 10, 15, 20, 25)

    print("Total:", total)
    print("Maximum:", max)