"""
Problem:
    Write a Radix MSD sorting algorithm

* Input = A list of non-negative integers
* Output = A sorted list of the same integers in ascending order.

Solution :
    The algorithm works by sorting the numbers based on each digit, starting from the most significant digit and moving towards the least significant digit.
"""
from typing import List


# --- Python Code --- #
def get_digit(num, d):
    return num // 10**d % 10


def recursive_radix_sort(A, n, d):
    if n <= 1 or d < 0:
        return A

    buckets = [[] for _ in range(10)]

    for num in A:
        buckets[get_digit(num, d)].append(num) if num >= 0 else buckets[get_digit(num, d)].append(num)

    __sorted = [num for bucket in reversed(buckets) for num in recursive_radix_sort(bucket, len(bucket), d - 1)]

    return __sorted


def radix_sort(A۲):
    max_num = max(abs(num) for num in A)
    max_digits = len(str(max_num))
    return recursive_radix_sort(A, len(A), max_digits-1)


if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    s = radix_sort(arr)
    print(s)
