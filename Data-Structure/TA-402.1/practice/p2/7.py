"""


"""

"""
1. Insertion Sort:
    Insertion Sort is stable because when you place an element in its correct position, 
    it only moves left as far as necessary. This means equal elements retain their original relative positions.
    
    
Example:
    Input:
    [(2, 'A'), (1, 'B'), (2, 'C'), (1, 'D')]
    
    Sorting by the first element (the numbers):
    
    After sorting (1, 'B'):
    [(1, 'B'), (2, 'A'), (2, 'C'), (1, 'D')]
    
    After sorting (1, 'D'):
    [(1, 'B'), (1, 'D'), (2, 'A'), (2, 'C')]
    
    Notice that (2, 'A') and (2, 'C') remain in the same order as they were originally.
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j][0] > key[0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [(2, 'A'), (1, 'B'), (2, 'C'), (1, 'D')]
print("Sorted array:", insertion_sort(arr))


"""
2. Bubble Sort
    Bubble Sort is stable because it only swaps adjacent elements if they are out of order. 
    This ensures that equal elements remain in the same relative order.
    
    
Example:
    Input:
    [(3, 'X'), (2, 'Y'), (2, 'Z'), (1, 'W')]
    
    After Bubble Sort, comparing pairs and swapping where necessary:
    
    After first pass:
    [(2, 'Y'), (2, 'Z'), (1, 'W'), (3, 'X')]
    
    After second pass:
    [(2, 'Y'), (1, 'W'), (2, 'Z'), (3, 'X')]
    
    Notice that (2, 'Y') and (2, 'Z') remain in their original relative order.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j][0] > arr[j+1][0]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [(3, 'X'), (2, 'Y'), (2, 'Z'), (1, 'W')]
print("Sorted array:", bubble_sort(arr))


"""
3. Merge Sort:
    Merge Sort is stable because during the merging process, when two elements are equal, the element from the left half (the earlier part of the array) is placed before the one from the right half, preserving their relative order.

Example:
    Input:
    [(5, 'A'), (3, 'B'), (5, 'C'), (1, 'D')]
    
    Split into sub-arrays:
    Left half: [(5, 'A'), (3, 'B')]
    Right half: [(5, 'C'), (1, 'D')]
    
    Recursively sort sub-arrays: Left: [(3, 'B'), (5, 'A')]
    Right: [(1, 'D'), (5, 'C')]
    
    Merge them:
    After merging, we get:
    [(1, 'D'), (3, 'B'), (5, 'A'), (5, 'C')]
    
    The elements (5, 'A') and (5, 'C') remain in the same order as in the input.
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i][0] <= right_half[j][0]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

arr = [(5, 'A'), (3, 'B'), (5, 'C'), (1, 'D')]
print("Sorted array:", merge_sort(arr))
