"""
Problem:
    Write a radix sorting algorithm to sort base 16 numbers (suggestion: convert the number to base 2)

* Input = A list of base 16 number
* Output = A sorted list of the same base 16 number in descending order.

Solution :
    convert to binary sort then convert back to base 16
"""


# --- Python Code --- #
def hex_to_dec(hex_list):
    dec_list = [int(num, 16) for num in hex_list]
    return dec_list


def dec_to_hex(dec_list):
    hex_list = [hex(num)[2:] for num in dec_list]
    return hex_list


def get_digit(num, d):
    return num // 10**d % 10


def recursive_radix_sort(A, n, d):
    if n <= 1 or d < 0:
        return A

    buckets = [[] for _ in range(10)]

    for num in A:
        buckets[get_digit(num, d)].append(num) if num >= 0 else buckets[get_digit(num, d)].append(num)

    __sorted = [num for bucket in reversed(buckets) for num in recursive_radix_sort(bucket, len(bucket), d - 1)]

    return __sorted


def radix_sort(A):
    A = hex_to_dec(A)
    max_num = max(abs(num) for num in A)
    max_digits = len(str(max_num))
    B = recursive_radix_sort(A, len(A), max_digits - 1)

    return dec_to_hex(B)


if __name__ == "__main__":

    hex_list = ['a', '2', 'f', '8', '3', '6', '9', 'c', '0', '5', 'b', 'e', '1', '4', '7', 'd']
    print("Original list:", hex_list)
    sorted_list = radix_sort(hex_list)
    print("Sorted list:", sorted_list)
