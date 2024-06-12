"""
Problem:
    Write a Radix MSD sorting algorithm for strings

* Input = A list of strings
* Output = A sorted list of the same strings in alphabetical order.

Solution :
    The algorithm works by sorting the strings based on each character, starting from the most significant character and
     moving towards the least significant character.
"""


# --- Python Code --- #
def get_char_index(s, i):
    return ord(s[i]) - ord('a') if i < len(s) else -1


def recursive_radix_sort(A, n, d):
    if n <= 1 or d >= max(len(s) for s in A):
        return A

    buckets = [[] for _ in range(32)]

    for s in A:
        buckets[get_char_index(s, d) + 1].append(s)

    return [s for bucket in buckets for s in recursive_radix_sort(bucket, len(bucket), d + 1)]


def radix_sort(A):
    return recursive_radix_sort(A, len(A), 0)


if __name__ == "__main__":
    arr = ["cat", "dog", "apple", "banana", "cherry"]
    sorted_arr = radix_sort(arr)
    print(sorted_arr)