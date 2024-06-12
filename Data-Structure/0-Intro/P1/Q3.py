"""
3.py:
    Write a program that, upon receiving a string, prints only the characters in the even indices
"""


def even_indices(__str):
    even_chars = ""
    for i in range(len(__str)):
        if i % 2 == 0:
            even_chars += __str[i]
    return f"Characters at even indices: {even_chars}"


if __name__ == "__main__":
    string_input = input("Enter a string : ")
    print(even_indices(string_input))