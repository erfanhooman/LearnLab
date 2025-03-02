"""
write Recursive LSD Radix Sort
"""

"""
Most Significant Digit (MSD) Radix Sort works by sorting numbers based on the most significant digit first and 
then recursively sorting smaller subgroups (buckets) based on their next significant digits. 
This is opposite to LSD (Least Significant Digit) Radix Sort, which processes numbers from the least significant to the most significant digit.

The MSD Radix Sort is particularly useful when dealing with strings or when the range of numbers is large. 
Let's implement this in Python for both positive and negative integers.
"""


def get_digit(number, d):
    """
    Get the d-th digit (from the left, counting from 0) of the number.
    For negative numbers, treat digits as positive.
    """
    return abs(number) // (10 ** d) % 10


def radix_sort_msd(arr, d=None):
    """
    MSD (Most Significant Digit) Radix Sort for an array of integers.
    """
    if len(arr) <= 1:  # Base case: A single element or empty array is already sorted
        return arr

    if d is None:
        # Find the maximum number to determine the number of digits to process
        max_value = max(abs(num) for num in arr)
        d = len(str(max_value)) - 1  # Highest digit to start sorting with

    if d < 0:
        return arr  # If no more digits to sort, return the array

    # Buckets for digits 0-9, plus a bucket for negatives (bucket 10)
    buckets = [[] for _ in range(11)]

    # Place each number in the corresponding bucket based on its d-th digit
    for number in arr:
        digit = get_digit(number, d)
        if number < 0:
            # Put negative numbers in a special bucket (bucket 10)
            buckets[10].append(number)
        else:
            # Put positive numbers in regular digit buckets
            buckets[digit].append(number)

    # Recursively sort each bucket (except negatives bucket) by the next most significant digit
    sorted_arr = []

    # First, handle negative numbers (special case, we need to sort them in reverse order)
    if buckets[10]:
        negative_bucket = radix_sort_msd(buckets[10], d - 1)
        sorted_arr.extend(negative_bucket)

    # Then handle digits 0-9 for positive numbers
    for i in range(10):
        if buckets[i]:
            sorted_arr.extend(radix_sort_msd(buckets[i], d - 1))

    return sorted_arr


# Test the function
arr = [170, -45, 75, -90, 802, 24, 2, 66]
sorted_arr = radix_sort_msd(arr)
print("Sorted array:", sorted_arr)
