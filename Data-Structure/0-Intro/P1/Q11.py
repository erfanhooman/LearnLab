"""
11.py:
    Write a program that separates the extension of a file after receiving the file name. (Hint: use the split function
    For example:
    input: hello.docx.txt
    output: txt
"""


def extract_file_extension(file_name):
    parts = file_name.split('.')

    # Check if there are at least two parts (name and extension)
    if len(parts) >= 2:
        return parts[-1]
    else:
        return "No extension found"


if __name__ == "__main__":
    file_name = input("Enter the file name: ")

    file_extension = extract_file_extension(file_name)

    print("extension:", file_extension)