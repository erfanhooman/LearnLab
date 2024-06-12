"""
page 23-2:
    write a radix sort algorithm in the recursive
"""


def radix_sort(arr):
    max_num = max(arr)
    radix = 1

    while radix <= max_num:
        bins = [[] for _ in range(10)]
        for x in arr:
            bins[(x // radix) % 10].append(x)

        arr = []
        for i in range(10):
            arr.extend(bins[i])

        radix *= 10

    return arr

