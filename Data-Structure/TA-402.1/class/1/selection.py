def selection_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


"""
Descending Order
"""































def selection_sort_descending(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Find the maximum element in the remaining unsorted array
        max_idx = i
        for j in range(i+1, n):
            if arr[j] > arr[max_idx]:  # Change comparison to arr[j] > arr[max_idx]
                max_idx = j
        # Swap the found maximum element with the first element
        arr[i], arr[max_idx] = arr[max_idx], arr[i]




