"""
Insertion Sort sorts by iterating through the array and placing each element into its correct position in the sorted part of the array.
"""

"""
During each insertion, we check if there exists a pair (arr[j], arr[i]) such that arr[j] + arr[i] = k.
We do this check with a set that stores elements of the sorted portion, and before inserting each element, 
we check if its complement (k - element) is already present in the set.
"""


def insertion_sort_and_check_sum(arr, k):
    # Create a set to keep track of seen elements in the sorted part
    seen = set()

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Before inserting the current key, check if (k - key) exists in the sorted part
        if (k - key) in seen:
            return arr, True  # If found, return early with True

        # Insert the current key into the sorted part
        arr[j + 1] = key

        # Add the current element to the seen set
        seen.add(arr[j + 1])

    return arr, False  # If no pair found, return False after sorting is done


def insertion_sort_and_check_sum_2(number, k):
    n = len(number)
    flag = False
    for i in range(n):
        for j in range(0, n - i - 1):
            if number[j] + number[j + 1] == k:
                flag = True
            if number[j] > number[j + 1]:
                number[j], number[j + 1] = number[j + 1], number[j]

    return flag, number


"""
- Bubble Sort compares adjacent elements and swaps them if they're out of order.
- During each comparison, we also check if any two numbers sum to k.
- We maintain a set of elements we've already processed in each pass, and as we compare and swap, 
    we check if the sum of the current element and any previously seen element is k.
"""


def bubble_sort_and_check_sum(arr, k):
    n = len(arr)
    # Set to track elements we've already processed
    seen = set()

    # Traverse through all array elements
    for i in range(n):
        swapped = False

        # Last i elements are already sorted
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

            # Check if the sum of arr[j] and any previously seen element equals k
            if (k - arr[j + 1]) in seen:
                return arr, True  # If found, return early with True

            # Add the element to the seen set after each comparison
            seen.add(arr[j])

        # Check for duplicates and sum with the final element in this pass
        if (k - arr[n - i - 1]) in seen:
            return arr, True

        # Add the final element in the current pass to the seen set
        seen.add(arr[n - i - 1])

        # If no elements were swapped, the array is already sorted
        if not swapped:
            break

    return arr, False  # If no pair found, return False after sorting is done
