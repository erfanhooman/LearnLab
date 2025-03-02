"""
p14.py:
    Get a list from the user, remove duplicate values and put them in a tuple, and finally the values
    Print its maximum and minimum

    Input example:
    sampleList = [87, 45, 41,87, 65, 94, 41, 99, 94,45]

    Example output:
    [87, 45, 41, 65, 94, 99]
    Min: 41
    Max: 99
"""


def process_list(input_list):
    list = [int(a) for a in set(input_list)]
    return sorted(list), min(list), max(list)


if __name__ == "__main__":
    try:
        list = input("Enter the list (comma-separated values): ").split(",")

        unique_list, min_value, max_value = process_list(list)

        print(unique_list)
        print(f"Min: {min_value}")
        print(f"Max: {max_value}")
    except ValueError:
        print("Input Must be Number")