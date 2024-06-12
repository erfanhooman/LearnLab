"""
Merge Sort is a widely used, efficient, and stable comparison-based sorting algorithm. It follows the divide-and-conquer
approach to sort a list of elements. The key idea behind Merge Sort is to divide the list into smaller sublists,
sort these sublists, and then merge them back together to create a sorted list. Merge Sort is known for its consistent
O(n log n) time complexity and is particularly useful for large datasets.

Here's the Merge Sort algorithm in a step-by-step explanation:

    1. Divide: The unsorted list is divided into two halves, usually by finding the middle index. This continues
    recursively until each sublist contains a single element.

    2. Conquer (Sort): The base case of the recursion sorts the sublists containing a single element because a single
    element is always considered sorted. Then, Merge Sort combines the sorted sublists in a way that results in a new
    sorted list. This involves repeatedly comparing and merging the elements of the two sublists into a new list,
    maintaining their sorted order.

    3. Combine (Merge)**: In this step, two sorted sublists are merged into a single sorted list. The merging process
    involves comparing elements from the two sublists and placing them in the correct order in a new temporary array.

    4. The process of dividing, sorting, and merging continues until there is only one sorted list, which is the final
    sorted result.

"""


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call to sort the two halves
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


"""
When we use Merge Sort ? 
    
    1. General-Purpose Sorting: Merge sort is a general-purpose sorting algorithm that can be used to sort an array or 
    list of elements of various data types. It's effective for sorting numbers, strings, objects, and more.
    
    2. Stable Sorting: Merge sort is a stable sorting algorithm, which means it maintains the relative order of equal 
    elements. This is important when you want to preserve the original order of items with the same value, such as sorting
     a list of people by their last names and then by their first names.
     
    3. Large Datasets: Merge sort's time complexity is O(n log n), where "n" is the number of elements to be sorted. 
     It provides consistent performance, even for large datasets. This makes it suitable for sorting a large amount of 
     data efficiently.
     
    4. External Sorting: Merge sort is commonly used for external sorting, which involves sorting data that does not 
     fit entirely in memory. It's efficient for sorting large files or datasets that need to be processed in chunks.
     
    5. Parallel Sorting: Merge sort can be adapted for parallel processing, allowing it to take advantage of multiple
      processors or cores. This can significantly speed up the sorting process.
      
    6. Online and Streaming Data: Merge sort can be used in scenarios where data is continuously arriving or streaming.
       It can be applied to maintain a sorted order as new data is added.
       
    7. Predictable Performance: Merge sort's performance is consistent and predictable, regardless of the input data. 
    This makes it a good choice when you need a sorting algorithm with reliable performance characteristics. 
    
    8. Custom Data Comparisons: Merge sort allows you to use custom comparison functions or criteria to sort data based 
    on specific attributes or properties of elements.
    
    9. Non-Comparison Sorts: Unlike many sorting algorithms that rely on element comparisons, merge sort can be adapted
    for non-comparison sorting tasks, such as sorting integers or floating-point numbers within a known range.
"""