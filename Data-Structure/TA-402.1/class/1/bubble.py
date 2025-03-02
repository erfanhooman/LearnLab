def bubble_sort(arr):
    n = len(arr)

    for i in range(n): # check all of the items

        # compare the first loop value with all of the items except itself and already sorted one
        for j in range(0, n-i-1):

            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


"""
Descending order
"""






























def bubble_sort_descending(arr):
    n = len(arr)
    # Traverse through all elements in the array
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is smaller than the next element
            if arr[j] < arr[j+1]:  # Change comparison to arr[j] < arr[j+1]
                arr[j], arr[j+1] = arr[j+1], arr[j]



