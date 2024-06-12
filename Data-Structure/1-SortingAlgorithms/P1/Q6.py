"""
Problem:
    Write a bucket sort algorithm to sort decimal numbers smaller than one to two decimal places

* Input = A list of decimal numbers smaller than one to two decimal places
* Output = A sorted list of the same numbers in ascending order.

Solution :
    Create a list of 100 buckets, for each possible value from 0.00 to 0.99 and then put each number in its own bucket
    then fill the empty list by adding the item of each bucket to the list
"""


# --- Pseudocode Code --- #

'''
- Initialize 100 empty buckets

- For each num in array
    Append number to relevant index bucket 

- Initialize empty list for sorted array and fill it with the buckets 

- For each sublist in buckets:
    For each num in sublist:
        Append num to list
'''
from typing import List


# --- Python Code --- #
def bucket_sort(arr):
    buckets = [[] for _ in range(100)]

    for num in arr:
        buckets[int(num * 100)].append(num)

    return [num for sublist in buckets for num in sublist]


if __name__ == "__main__":
    arr = [0.12, 0.14, 0.18, 0.16, 0.22]
    sorted_arr = bucket_sort(arr)
    print(sorted_arr)
