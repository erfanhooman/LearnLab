"""
Yes , Insertion sort, bubble sort and merge sort is stable
    for example :

    [(4, 'A'), (3, 'B'), (3, 'A'), (5, 'B'), (4, 'B'), (5, 'A')]
    
    if we get this to the sorting algoritms we going to have :
        [(3, 'B'), (3, 'A'), (4, 'A'), (4, 'B'), (5, 'B'), (5, 'A')]
                                                                in the output
                                                                
    as u can see (3, 'B') and (3, 'A') are in the same order of the input

"""

arr = [(4, 'A'), (3, 'B'), (3, 'A'), (5, 'B'), (4, 'B'), (5, 'A')]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key[0] < arr[j][0]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index][0] <= right[right_index][0]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged += left[left_index:]
    merged += right[right_index:]
    return merged


if __name__ == "__main__":
    sorted_by_insertion_sort = insertion_sort(arr.copy())
    sorted_by_bubble_sort = bubble_sort(arr.copy())
    sorted_by_merge_sort = merge_sort(arr.copy())

    print("Original list:", arr)
    print("Sorted by Insertion Sort:", sorted_by_insertion_sort)
    print("Sorted by Bubble Sort:", sorted_by_bubble_sort)
    print("Sorted by Merge Sort:", sorted_by_merge_sort)
