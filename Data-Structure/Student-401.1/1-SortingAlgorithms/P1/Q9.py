"""
Problem:
    Write a Radix sorting algorithm for positive and negative number

* Input = A list of integers
* Output = A sorted list of the same integers in ascending order.
"""

# --- Python Code --- #


def get_digit(num, d):
    return num // 10**d % 10


def recursive_radix_sort(A, n, d):
    if n <= 1 or d < 0:
        return A

    pos_buckets = [[] for _ in range(10)]
    neg_buckets = [[] for _ in range(10)]

    for num in A:
        pos_buckets[get_digit(num, d)].append(num) if num >= 0 else neg_buckets[get_digit(num, d)].append(num)

    sorted_neg = [num for bucket in reversed(neg_buckets) for num in recursive_radix_sort(bucket, len(bucket), d - 1)]
    sorted_pos = [num for bucket in pos_buckets for num in recursive_radix_sort(bucket, len(bucket), d - 1)]

    return sorted_neg + sorted_pos


def radix_sort(A):
    max_num = max(abs(num) for num in A)
    max_digits = len(str(max_num))
    return recursive_radix_sort(A, len(A), max_digits-1)


if __name__ == "__main__":
    arr = [170, 45, -75, -90, 802, 24, 2, -66]
    sorted_arr = radix_sort(arr)
    print(sorted_arr)
