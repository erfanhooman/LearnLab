"""
Modify merge sort so that all even numbers appear first in sorted order, followed by odd numbers also in sorted order.
"""

"""
In the merge process, modify it to place all even numbers on the left side and odd numbers on the right. After merging 
both sub-arrays, just handle them normally based on their parity.
"""


# Function to merge two sub-arrays in such a way that all even numbers come first,
# followed by odd numbers, while maintaining sorted order within each group (evens, odds).
def merge_even_odd(arr, temp_arr, left, mid, right):
    i = left  # Starting index for the left sub-array (evens/odds)
    j = mid + 1  # Starting index for the right sub-array (evens/odds)
    k = left  # Starting index for the temporary array

    # Merge the two sub-arrays while placing even numbers first.
    while i <= mid and j <= right:
        # Case 1: If current left element is even and (right is odd or left <= right)
        # we take the left element.
        if arr[i] % 2 == 0 and (arr[j] % 2 != 0 or arr[i] <= arr[j]):
            temp_arr[k] = arr[i]
            i += 1
        # Case 2: If current right element is even and left element is odd, we take the right element.
        elif arr[j] % 2 == 0 and arr[i] % 2 != 0:
            temp_arr[k] = arr[j]
            j += 1
        # Case 3: Otherwise, handle remaining cases:
        # - If both are even, take the smaller one.
        # - If both are odd, take the smaller one.
        # In case of mixed even/odd, take the appropriate one based on parity first.
        else:
            temp_arr[k] = arr[j] if arr[j] % 2 == 0 else arr[i]
            # Depending on which condition matched, we update i or j.
            j, i = j + 1 if arr[j] % 2 == 0 else i + 1, i + 1 if arr[i] % 2 != 0 else i
        k += 1

    # Copy any remaining elements from the left sub-array (these would all be even).
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right sub-array (even or odd).
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1

    # Copy the sorted sub-array back into the original array.
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]


# Recursive function that performs merge sort, but using our modified merge function.
def merge_sort_even_odd(arr, temp_arr, left, right):
    if left < right:
        # Find the middle point to divide the array into two halves.
        mid = (left + right) // 2

        # Recursively sort the first and second halves.
        merge_sort_even_odd(arr, temp_arr, left, mid)
        merge_sort_even_odd(arr, temp_arr, mid + 1, right)

        # Merge the two sorted halves using our custom merge function.
        merge_even_odd(arr, temp_arr, left, mid, right)


# Function that initiates the sorting of the array with even numbers first and odd numbers later.
def sort_even_odd(arr):
    temp_arr = [0] * len(arr)  # Temporary array to assist in merging.
    merge_sort_even_odd(arr, temp_arr, 0, len(arr) - 1)  # Start the merge sort process.
