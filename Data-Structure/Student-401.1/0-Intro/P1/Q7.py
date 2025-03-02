"""
7.py:
    Write a program that receives the radius of the circle, displays its perimeter and area with appropriate output
"""

import math


def calculate_circle(radius):
    if radius <= 0:
        raise ValueError

    perimeter = 2 * math.pi * radius
    area = radius * radius * math.pi

    return perimeter, area


if __name__ == "__main__":
    try:
        radius = float(input("enter the radius : "))
        perimeter, area = calculate_circle(radius)

        print(f"the perimeter of the circle is {perimeter:.3f}")
        print(f"the area of the circle is {area:.3f}")

    except ValueError:
        print("Invalid input. Please enter a positive integer for radius")