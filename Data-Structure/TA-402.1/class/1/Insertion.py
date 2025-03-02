"""Insertion Sort"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j-1]
            j -= 1


"""Descending Order"""

































def insertion_sort_descending(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] > arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j-1]
            j -= 1

