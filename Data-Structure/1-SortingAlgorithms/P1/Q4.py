"""
Problem:
    Write a program that receives an array of n elements from the user, as well as a number such as x, in addition to
    sorting the array using the insertion sort, it also checks whether two numbers in this array
    exist whether their sum equals x or not

* Input = A list of number and x
* Output = Sorted array and the Bool

Solution :
    put the flag false , loop over all element and check if the two element addition is x make flag True
"""


# --- Python Code --- #
def improved_insertion_sort(arr, x):
    flag = False
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        for k in range(0, i):
            if arr[k] + arr[i] == x:
                flag = True
                break

    return flag


if __name__ == "__main__":
    arr = [4, 3, 2, 10]
    flag = improved_insertion_sort(arr, 12)
    print(flag)