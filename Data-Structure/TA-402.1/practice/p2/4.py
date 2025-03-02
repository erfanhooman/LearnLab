"""
Modify merge sort to stop once it finds the
k-th largest element in the array instead of sorting the whole array.
"""

"""
- During the merge phase, as elements are moved into their final positions, we'll keep a counter.
- When the counter reaches l, meaning that we've sorted the k-th element (or sorted l elements in total), 
    we'll return the current state of the array.
    
"""


# Helper function to merge two sorted sub-arrays and track the number of elements sorted
def merge_kth_element(arr, temp_arr, left, mid, right, l, sorted_count):
    i = left  # Starting index for left sub-array
    j = mid + 1  # Starting index for right sub-array
    k = left  # Starting index for the merged sub-array

    # Merge the two sub-arrays
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            j += 1
        k += 1
        # Increment sorted_count for each element placed in the correct position
        sorted_count += 1
        if sorted_count == l:
            # If we've sorted the l-th element, return the current state of the array
            return arr, True, sorted_count

    # Copy remaining elements of the left sub-array, if any
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
        sorted_count += 1
        if sorted_count == l:
            return arr, True, sorted_count

    # Copy remaining elements of the right sub-array, if any
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
        sorted_count += 1
        if sorted_count == l:
            return arr, True, sorted_count

    # Copy the merged sub-array back into the original array
    for i in range(left, right + 1):
        arr[i] = temp_arr[i]

    # Return False to indicate we haven't sorted the l-th element yet
    return arr, False, sorted_count


# Recursive function to perform merge sort and track when the l-th element is sorted
def merge_sort_kth_element(arr, temp_arr, left, right, l, sorted_count):
    if left < right:
        mid = (left + right) // 2

        # Sort the first half and check if the l-th element is sorted
        arr, done, sorted_count = merge_sort_kth_element(arr, temp_arr, left, mid, l, sorted_count)
        if done:
            return arr, True, sorted_count

        # Sort the second half and check if the l-th element is sorted
        arr, done, sorted_count = merge_sort_kth_element(arr, temp_arr, mid + 1, right, l, sorted_count)
        if done:
            return arr, True, sorted_count

        # Merge the two sorted halves and check if the l-th element is sorted
        arr, done, sorted_count = merge_kth_element(arr, temp_arr, left, mid, right, l, sorted_count)
        if done:
            return arr, True, sorted_count

    return arr, False, sorted_count


# Function to start the modified merge sort and return when the l-th element is sorted
def sort_until_kth(arr, l):
    temp_arr = [0] * len(arr)
    sorted_count = 0  # Tracks the number of elements sorted so far
    arr, done, _ = merge_sort_kth_element(arr, temp_arr, 0, len(arr) - 1, l, sorted_count)
    return arr  # Return the array after sorting the l-th element
