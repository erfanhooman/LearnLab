"""
Insertion Sort is a simple comparison-based sorting algorithm that builds the final sorted array one item at a time.
It is particularly efficient for small datasets or nearly sorted datasets.
The algorithm works by repeatedly taking one element from the unsorted portion of the array and inserting it into
its correct position within the sorted portion of the array.

Here's the Insertion Sort algorithm in a step-by-step explanation:

    1. Start with the second element (index 1) in the array. The first element is considered to be in the sorted portion
    by itself.

    2. Compare the second element with the one before it (element at index 0) and insert it into its correct position
    within the sorted portion. If the element is smaller, swap them.

    3. Move on to the third element (index 2) and insert it into the sorted portion by shifting the larger elements to
    the right until the correct position is found.

    4. Continue this process for all remaining elements in the array until the entire array is sorted.

"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j - 1], arr[j] = arr[j], arr[j-1]
            j -= 1


# Example usage:
arr = [12, 11, 13, 5, 6]
insertion_sort(arr)
print("Sorted Array:", arr)


"""
When we use insertion sort ? 
    1. Small Input Sizes: Insertion sort is most efficient when sorting small input sizes. This is because it has a 
    relatively low overhead, and for small arrays or lists, its time complexity is quite reasonable.
    
    2. Partially Sorted Data: When a significant portion of the data is already sorted or nearly sorted, insertion sort 
    can be very efficient. It has an adaptive characteristic, meaning its performance improves for partially sorted data.
    
    3. Online Sorting: In situations where data is continuously arriving or streaming, insertion sort can be useful. 
    It allows you to insert each new element into the sorted portion of the data as it arrives, making it a suitable 
    choice for online or real-time sorting.
    
    4. Stable Sorting: Insertion sort is a stable sorting algorithm, meaning it maintains the relative order of equal 
    elements. If you require a stable sorting algorithm, insertion sort can be a good choice.
    
    5. Small Overhead: Insertion sort has a relatively low constant factor and is easy to implement. 
    If simplicity and low overhead are more important than sorting efficiency, insertion sort can be a practical choice.
    
    6. Educational Purposes: Insertion sort is often used in educational contexts to teach the concept of sorting algorithms.
     It's straightforward and easy to understand, making it a good starting point for learning about sorting.
"""