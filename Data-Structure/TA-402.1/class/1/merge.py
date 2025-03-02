def merge_sort(arr):
    """
    This line checks if the array has more than one element. If it has only one element (or none), it's already sorted, and the function doesn't need to do anything.
    """
    if len(arr) > 1:

        # Divide the array elements into two halves
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        # i is used to track the current element in left_half.
        # j is used to track the current element in right_half.
        # k is used to track the position in the original array (arr
        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # after the main loop, there might still be some elements left in the left_half, or right in right_half
        # This while loop takes care of copying any remaining elements from left_half into the main array (arr).
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


"""
Descending order
"""









def merge_sort_descending(arr):
    if len(arr) > 1:
        # Find the middle of the array
        mid = len(arr) // 2

        # Divide the array elements into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursively sort the two halves
        merge_sort_descending(left_half)
        merge_sort_descending(right_half)

        # Initialize pointers for left_half, right_half, and the merged array
        i = j = k = 0

        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] > right_half[j]:  # Change comparison to left_half[i] > right_half[j]
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Check if any element is left in the left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Check if any element is left in the right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
