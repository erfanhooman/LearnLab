"""
2.py:
    Change the bubble sort algorithm in such a way that the array is sorted in descending order and in two ways:
"""


# A : By moving the largest element to the beginning of the array in each round
def improved_bubble_sort_A(arr):
    n = len(arr)

    for j in range(n - 1):
        for i in range(n - 1, j, -1):
            if arr[i] > arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]


# B : By moving the smallest element to the end of the array in each round
def bubble_sort_improved_B(arr):
    n = len(arr)

    for j in range(n - 1):
        for i in range(1, n - j):

            if arr[i] > arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]


if __name__ == "__main__":
    arr = [5, 1, 12, -5, 16]

    improved_bubble_sort_A(arr)
    # bubble_sort_improved_B(arr)

    print(arr)