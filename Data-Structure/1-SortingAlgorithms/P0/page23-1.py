"""
page 23-1:
    Write a bucket sort algorithm to sort positive and negative two-digit numbers
"""


def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


def bucket_sort(A):

    positive_items = [[] for _ in range(len(A))]
    negative_items = [[] for _ in range(len(A))]

    for a in A:
        if a >= 0:
            positive_items[a // 10].append(a)
        else:
            negative_items[-a // 10].append(a)

    for i in range(10):
        positive_items[i] = bubble_sort(positive_items[i])
        negative_items[i] = bubble_sort(negative_items[i])

    sorted_array = []
    for bin in negative_items:
        sorted_array.extend(bin)
    for bin in positive_items:
        sorted_array.extend(bin)

    return sorted_array


if __name__ == "__main__":
    A = [0, 1, 11, 30, 64, 40, 50, 80, 88, 99, 13, -5, -23, -10, -2]
    sorted_A = bucket_sort(A)
    print("Sorted array:", sorted_A)