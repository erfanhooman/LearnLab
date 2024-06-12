"""
--A--
Problem :
    By changing the insertion sort algorithm, sort the input array by removing duplicate elements

* Input : A list of number
* Output : A sorted list of the same number in ascending order

Solution :
    In the insertion sort algorithm with shift the element to right check if the element is same pop the element


--B--
Problem B :
    By changing the bubble sort algorithm, sort the input array by removing duplicate elements

* Input : A list of number
* Output : A sorted list of the same number in ascending order

Solution :
    In the bubble sort after sorting the array loop over and check if the number is same with the next one pop the
    element
"""


# --- Python Code --- #

def improved_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j>=0:
            if key < arr[j]:
                arr[j+1] = arr[j]
            elif key == arr[j]:
                arr.pop(j)
            else:
                break
            j -= 1

        arr[j + 1] = key


def improved_bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    i = 0
    while i < len(arr) - 1:
        if arr[i] == arr[i + 1]:
            arr.pop(i)
        else:
            i += 1


if __name__ == "__main__":
    arr = [12, 11, 12, 5, 6, 12, 5]
    improved_insertion_sort(arr)
    improved_bubble_sort(arr)
    print(arr)
