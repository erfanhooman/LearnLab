import random
import time
from typing import List


# Insertion Sort
def insertion_sort(nums):
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


# Merge Sort
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    sorted_list = []
    while len(left_list) > 0 and len(right_list) > 0:
        if left_list[0] <= right_list[0]:
            sorted_list.append(left_list.pop(0))
        else:
            sorted_list.append(right_list.pop(0))
    if len(left_list) > 0:
        sorted_list += left_list
    if len(right_list) > 0:
        sorted_list += right_list
    return sorted_list


# Radix Sort
def counting_sort(nums, digit):
    size = len(nums)
    output = [0] * size
    count = [0] * 10
    for i in range(size):
        index = nums[i] // digit
        count[int(index % 10)] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = size - 1
    while i >= 0:
        index = nums[i] // digit
        output[count[int(index % 10)] - 1] = nums[i]
        count[int(index % 10)] -= 1
        i -= 1
    for i in range(size):
        nums[i] = output[i]
    return nums


def radix_sort(nums: List[float]) -> List[float]:
    nums = [int(num * 100) for num in nums]
    max_num = max(nums)
    digit = 1
    while max_num / digit > 0:
        nums = counting_sort(nums, digit)
        digit *= 10
    nums = [num / 100 for num in nums]
    return nums


"""
    Merge Sort seems to sort faster because it doesn't compare all the numbers and by categorizing, reduces the number
     of if steps
"""


# Generate random numbers
original_numbers = [round(random.uniform(0, 1), 2) for _ in range(100000)]


# Measure execution time
numbers = original_numbers.copy()
start_time = time.time()
insertion_sort(numbers)
print(f"Insertion Sort: {time.time() - start_time}")

numbers = original_numbers.copy()
start_time = time.time()
merge_sort(numbers)
print(f"Merge Sort: {time.time() - start_time}")

numbers = original_numbers.copy()
start_time = time.time()
radix_sort(numbers)
print(f"Radix Sort: {time.time() - start_time}")


"""
Merge Sort > Radix sort > Insertion Sort
"""