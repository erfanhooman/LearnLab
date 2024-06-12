"""
6.py:
    Write a program that by receiving a positive integer and a string from the user,
     the number of received numbers will be output in the output Copy the input string,
      example : n=3 and 'hello='1str, output equal to 'hellohellohello'
"""


def repeat_string(num, __str):
    if num <= 0:
        raise ValueError

    result = __str * num
    return result


if __name__ == "__main__":
    try:
        n = int(input("Enter a positive integer: "))
        text = input("Enter a string: ")
        repeated_text = repeat_string(n, text)
        print("Output:", repeated_text)
    except ValueError:
        print("Invalid input. Please enter a positive integer for n")