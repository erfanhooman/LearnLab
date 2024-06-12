"""
12.py:
    Write a program that receives two date numbers and displays the difference in the number of days
    use date() function
"""

from datetime import date


def calculate_date_difference(date1, date2):
    year1, month1, day1 = map(int, date1.split("-"))
    year2, month2, day2 = map(int, date2.split("-"))

    date_obj1 = date(year1, month1, day1)
    date_obj2 = date(year2, month2, day2)

    date_difference = (date_obj2 - date_obj1).days

    return date_difference


if __name__ == "__main__":
    date1 = input("Enter the first date (YYYY-MM-DD): ")
    date2 = input("Enter the second date (YYYY-MM-DD): ")

    try:
        difference = calculate_date_difference(date1, date2)
        print(f"Difference in days: {difference} days")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD format.")
