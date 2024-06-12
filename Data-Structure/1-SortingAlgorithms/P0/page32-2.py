"""
page 23-2:
    Use Radix sorting algorithm to sort hex number
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


def radix_sort_hex(arr):
    max_num = max(arr, key=lambda x: int(x, 16))
    max_len = len(max_num)
    radix = 1

    while radix <= max_len:
        bins = [[] for _ in range(16)]

        for x in arr:
            digit = int(x[-radix], 16) if radix <= len(x) else 0
            bins[digit].append(x)

        arr = []
        for i in range(16):
            arr.extend(bins[i])

        radix += 1

    return arr


if __name__ == "__main__":
    hex_numbers = ["1A", "3F", "0B", "2D", "15", "29", "4C", "11", "0F"]
    sorted_numbers = radix_sort_hex(hex_numbers)
    print("Sorted hexadecimal numbers:", sorted_numbers)

    A = [163, 456, 782, 345, 123, 987, 341, 670, 987, 1234, 6547, 9865]
    a = radix_sort(A)
    print(a)