def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume the current index is the minimum
        min_idx = i

        # Find the minimum element in the unsorted portion of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element in the unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array is:", arr)