"""
Problem:
    Write a recursive Radix LSD sorting algorithm

* Input = A list of non-negative integers
* Output = A sorted list of the same integers in ascending order.

Solution :
    sorting the numbers based on each digit, starting from the least significant digit and moving towards the most
    significant digit.
"""


# --- Pseudocode Code --- #

'''
- If n is less than or equal to 1 or d is less than 0
    Return A
    
-Initialize 10 empty buckets

-For each num in A
    Append num to the bucket corresponding to the digit at position d of num
    
-Initialize an empty list sorted

-For each bucket in buckets
    Append RecursiveRadixSort(bucket, length of bucket, d-1) to sorted
    
Return sorted
'''
from typing import List


# --- Python Code --- #
def get_digit(num, d):
    return num // 10**d % 10


def recursive_radix_sort(A, n, d):
    if n <= 1 or d < 0:
        return A
    buckets = [[] for _ in range(10)]
    for num in A:
        buckets[get_digit(num, d)].append(num)

    __sorted = [num for bucket in buckets for num in recursive_radix_sort(bucket, len(bucket), d - 1)]

    return __sorted


def radix_sort(A):
    max_num = max(A)
    max_digits = len(str(max_num))
    return recursive_radix_sort(A, len(A), max_digits-1)


if __name__ == "__main__":
    arr = [170, 45, 75, 90, 802, 24, 2, 66]
    sorted_arr = radix_sort(arr)
    print(sorted_arr)