"""
4.py:
    Write a program that, upon receiving a string and index, removes the character in that index from the string
"""


def remove_character_at_index(__str, index):
    if 0 <= index < len(__str):
        modified_string = __str[:index] + __str[index+1:]
        return modified_string
    raise TypeError


if __name__ == "__main__":
    input_string = input("Enter a string : ")

    try:
        index = int(input("Enter an index : "))
        print(f"result : {remove_character_at_index(input_string, index)}")
    except ValueError:
        print("The Index Must be integer")
    except TypeError:
        print("Index is out of range")
