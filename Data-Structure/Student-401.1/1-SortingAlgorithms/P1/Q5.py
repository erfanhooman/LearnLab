"""
Problem:
    Write a bucket sort algorithm to sort positive and negative two-digit numbers

* Input = A list of positive and negative two-digit number
* Output = A sorted list of the same numbers in ascending order.

Solution :
    Create a list of 20 bucket, for each positive and negative two-digit numbers and then put each number in own bucket
    then fill the empty list by adding the item of each bucket to the list
"""


# --- Pseudocode Code --- #

'''
- Initialize 20 empty positive buckets
- Initialize 20 empty negative buckets

- For each num in array
    If num is positive
      Append number to relevant index positive bucket 
    Else (num is negative)
        Append number to relevant index negative bucket 

- Initialize empty list for sorted array and fill it with the positive bucket and then negative bucket 

- For each sublist in negative buckets:
    For each num in sublist:
        Append num to list
        
- For each sublist in positive buckets:
    For each num in sublist:
        Append num to list
'''
from typing import List


# --- Python Code --- #
def bucket_sort(arr):
    pos_buckets = [[] for _ in range(20)]
    neg_buckets = [[] for _ in range(20)]

    for num in arr:
        pos_buckets[num // 10].append(num) if num >= 0 else neg_buckets[abs(num) // 10].append(num)

    return [num for sublist in neg_buckets for num in sublist] + [num for sublist in pos_buckets for num in sublist]


if __name__ == "__main__":
    arr = [12, -14, 18, 16, -22]
    __sorted = bucket_sort(arr)
    print(__sorted)