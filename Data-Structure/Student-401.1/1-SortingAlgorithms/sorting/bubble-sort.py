"""
Bubble Sort is a simple comparison-based sorting algorithm that repeatedly steps through the list, compares adjacent
elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.
It gets its name from the way smaller elements "bubble" to the top of the list during each pass.

Here's the Bubble Sort algorithm in a step-by-step explanation:

    1. Start with the first element in the list.

    2. Compare it with the next element. If the first element is greater than the second element, swap them.

    3. Move on to the next element and compare it with the element following it. Continue this process until you reach
    the end of the list. At the end of the first pass, the largest element will have "bubbled up" to the end of the list.

    4. Repeat steps 1-3 for the entire list, but now ignore the last element since it is already in its correct sorted
    position.

    5. Continue this process, each time ignoring one more element from the end of the list, until the entire list is
    sorted.

"""


def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


"""
When we Use Bubble sort ?
    1. Educational Purposes: Bubble sort is often introduced in computer science courses as a simple sorting algorithm to 
    help students understand the basics of sorting and algorithms. It is a straightforward algorithm to implement and 
    can serve as a learning tool for those new to programming and algorithms.
    
    2. Small Datasets: In cases where you have a very small dataset, bubble sort can be used without a significant 
    impact on performance. When the dataset is tiny, the simplicity of the algorithm may outweigh its inefficiency.
    
    3. Already Mostly Sorted Data: Bubble sort performs well on data that is already nearly sorted. In such cases, 
    it may require only a few passes to complete the sorting, making it more efficient compared to other algorithms.
    
    4. Implementation Constraints: In embedded systems or very limited environments where memory and processing power are
     extremely constrained, bubble sort may be chosen because it is simple and can be implemented with minimal resources.
"""