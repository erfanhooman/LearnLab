"""
if we have a tuple like this
    [(4, 'A'), (3, 'B'), (3, 'A'), (5, 'B'), (4, 'B'), (5, 'A')]
        after we sort the tuple we going to have
            [(3, 'A'), (3, 'B'), (4, 'A'), (4, 'B'), (5, 'A'), (5, 'B')]

    and its not stable we can make the selection sort like this :
"""


def stable_selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index][0] > arr[j][0]:
                min_index = j

        key = arr[min_index]
        while min_index > i:
            arr[min_index] = arr[min_index - 1]
            min_index -= 1
        arr[i] = key

    return arr


if __name__ == "__main__":
    arr = [(4, 'A'), (3, 'B'), (3, 'A'), (5, 'B'), (4, 'B'), (5, 'A')]
    print(stable_selection_sort(arr))
