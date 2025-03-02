"""
Selection Sort is a simple comparison-based sorting algorithm that works by dividing the input list into two parts:
the sorted part and the unsorted part. It repeatedly selects the minimum (or maximum) element from the unsorted part
and moves it to the end of the sorted part. The algorithm continues this process until the entire list is sorted.

Here's the Selection Sort algorithm in a step-by-step explanation:

1. Start with the entire list as unsorted.

2. Find the minimum (or maximum) element in the unsorted portion of the list.

3. Swap the found minimum element with the first element in the unsorted portion.

4. Move the boundary between the sorted and unsorted portions one element to the right.

5. Repeat steps 2-4 until the entire list is sorted.
"""


def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        # Assume the current index is the minimum
        min_idx = i

        # Find the minimum element in the unsorted portion of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element in the unsorted portion
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array is:", arr)


"""
when we use selection sort ?

    1. Educational Purposes: Selection sort is often introduced as one of the first sorting algorithms in computer 
    science and programming courses. It provides a basic understanding of sorting algorithms and their time complexity 
    analysis.
    
    2. Small Lists or Arrays: Selection sort can be efficient for very small lists or arrays. In situations where the 
    input size is small, the overhead of more complex sorting algorithms might outweigh the benefits of a simpler 
    algorithm like selection sort.
    
    3. Simple Implementations: Selection sort has a straightforward and easy-to-understand implementation. 
    It involves minimal code and is easy to explain, making it suitable for teaching or learning about sorting algorithms.
    
    4. Stable Sorting: Selection sort is a stable sorting algorithm, which means it maintains the relative order of equal 
    elements. In situations where stability is required, selection sort can be chosen.
    
    5. In-Place Sorting: Selection sort operates in-place, meaning it does not require additional memory for sorting.
     This can be useful in situations with memory constraints.
     
     6. Sorting Small Sub arrays: Selection sort can be used as a component in more complex sorting algorithms, 
     such as quicksort. It is often employed to sort small sub arrays when partitioning data for quicksort.
"""