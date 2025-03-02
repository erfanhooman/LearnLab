"""
5.py
    Write a program that by receiving two numbers a and b, divide, add and power them (b^a, b/a, b+a)
    and them print them with appropriate message
"""


def operations(a, b):
    division_result = b / a
    addition_result = b + a
    power_result = b ** a
    return division_result, addition_result, power_result


if __name__ == "__main__":
    try:
        a = float(input("Enter the value of a: "))
        b = float(input("Enter the value of b: "))

        division_result, addition_result, power_result = operations(a, b)

        print("Results:")
        print(f"{b} divided by {a} is: {division_result}")
        print(f"{b} plus {a} is: {addition_result}")
        print(f"{b} raised to the power of {a} is: {power_result}")

    except ValueError:
        print("Invalid input. Please enter numeric values for a and b.")
