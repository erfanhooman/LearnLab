"""
In Insertion Sort, the array is sorted one element at a time by comparing each element with the already sorted portion.
"""

"""
In Insertion Sort, the array is sorted one element at a time by comparing each element with the already sorted portion. 
We can modify the process to check for duplicates during insertion and skip adding them to the sorted part if they already exist.


- Start from the second element and iterate through the array.
- For each element, find its position in the already sorted part of the array.
- As you shift elements to the right to make space, check if the element already exists. If it does, remove the duplicate by not inserting it.
- Continue this process for all elements.
- At the end, return the sorted array with duplicates removed.
"""


def insertion_sort_remove_duplicates(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Check for duplicates before inserting the key
        if arr[j] != key:  # arr[j] is now the element just before the insertion point
            arr[j + 1] = key  # Insert the key at the correct position
        else:
            # If there's a duplicate, remove the current element
            arr.pop(i)  # Removing duplicates at the current index

    return arr


"""
In Bubble Sort, the array is sorted by repeatedly swapping adjacent elements if they are in the wrong order. 
We can modify this process to check for duplicates during the comparison and remove them when found.

- Perform the usual bubble sort comparisons.
- As you swap elements, check if the adjacent elements are duplicates.
- If a duplicate is found, remove the element and continue with the sorting process.
- Repeat this process for each pass over the array.
-After sorting, return the array with duplicates removed.
"""


def bubble_sort_remove_duplicates(arr):
    n = len(arr)

    # Traverse through all array elements
    i = 0
    while i < n:
        swapped = False
        j = 0
        while j < n - i - 1:
            # Check for duplicates and remove the duplicate
            if arr[j] == arr[j + 1]:
                arr.pop(j + 1)
                n -= 1  # Reduce the size of the array
                swapped = True  # Array changed due to pop

            # Swap if the element found is greater than the next element
            elif arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                j += 1  # Move to the next element

            else:
                j += 1  # Only move forward if no swap or pop

        # If no elements were swapped, the array is already sorted
        if not swapped:
            break

        i += 1

    return arr
