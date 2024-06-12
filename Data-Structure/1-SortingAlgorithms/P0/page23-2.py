"""
page 23-2:
    Using bucket sorting algorithm, decimal numbers smaller than one
    Arrange the two decimal places
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


def bucket_sort(numbers):
    bins = [[] for _ in range(len(numbers))]

    for num in numbers:
        index = int(num * len(numbers))
        bins[index].append(num)

    for i in range(100):
        bins[i] = bubble_sort(bins[i])

    sorted_array = []
    for bin in bins:
        sorted_array.extend(bin)

    return sorted_array


if __name__ == "__main__":
    decimal_numbers = [0.23, 0.11, 0.45, 0.08, 0.99, 0.37, 0.64, 0.52]
    sorted_numbers = bucket_sort(decimal_numbers)
    print("Sorted decimal numbers:", sorted_numbers)
