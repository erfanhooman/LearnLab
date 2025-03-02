"""
Radix Sort is a non-comparative sorting algorithm that works by processing elements based on their individual digits or
characters. It's commonly used for sorting integers and strings. The algorithm processes elements from the least
significant digit (rightmost) to the most significant digit (leftmost) or vice versa, sorting the elements based on each
digit's value.
"""


def flaten(list):
    a = []
    for item in list:
        a.extend(item)
    return a


def radix_sort_LSD(arr, max_digit):
    for i in range(max_digit):
        buckets = [[] for _ in range(10)]

        for item in arr:
            num = item // 10 ** i % 10
            buckets[int(num)].append(item)

        arr = flaten(buckets)
    return arr


arr = [225, 315, 221, 311, 326, 216]
max_digit = len(str(max(arr)))
arr = radix_sort_LSD(arr, max_digit)
print(arr)

"""
When we use radix sort ? 
    1. Fixed-Length Integer Sorting: Radix Sort is highly effective when sorting a list of fixed-length integers. 
    Since it processes elements based on individual digits, it's ideal for sorting integers that have the same number of
    digits (e.g., 3-digit integers).
    
    2. Strings: Radix Sort can also be used for sorting strings. It sorts strings character by character from right to 
    left or left to right, depending on the desired order.
    
    3. Non-Comparative Sorting: Unlike comparison-based sorting algorithms (e.g., Quick Sort or Merge Sort), Radix Sort 
    does not rely on comparing elements to determine their order. It's suitable for non-comparable data, such as integers
     and strings.
     
     4. External Sorting: Radix Sort is useful for external sorting when data is too large to fit into memory. 
     It can be applied to sort large datasets that don't fit entirely in RAM.
     
     5. Parallel Processing: Radix Sort can be parallelized, making it efficient for distributed or multi-core processing
     environments. Each digit place can be processed independently.
     
     6. Stable Sorting: Radix Sort is inherently stable, which means it preserves the relative order of equal elements.
     This can be an advantage in certain applications.
     
     7. Uniformly Distributed Data: It's most efficient when the input data is uniformly distributed across a range of 
     values. In such cases, the elements are evenly spread out, making it possible to divide the range into multiple buckets.
     
     8. Known Range of Values: Radix Sort is suitable when you know the range of values that the input can take. 
     This allows you to predefine the range and create buckets accordingly.
     
     9. Close to Uniform Distribution: Even if the data is not perfectly uniformly distributed, Radix Sort can still 
     work well if the distribution is reasonably close to uniform. It can handle some variability in the data.
"""
