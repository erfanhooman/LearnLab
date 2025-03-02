"""
Counting Sort is a sorting algorithm that is non-comparative and works well when you have a limited range of input
values. It is an efficient sorting algorithm for sorting integers or objects with integer keys. Counting Sort works
by counting the frequency of each distinct element in the input, and then using that information to place each element
in its correct sorted position.

Here's the Counting Sort algorithm in a step-by-step explanation:

    1. Find the range of input values: Determine the minimum and maximum values in the input array. This information is
    used to set up a counting array.

    2. Create a counting array: Create an auxiliary array, often called the "counting array," of size equal to the
    range of input values (max - min + 1). Initialize all elements in this array to 0.

    3. Count the occurrences: Iterate through the input array and, for each element, increment the corresponding index
    in the counting array. For example, if you encounter the value 5 in the input array, you would increment the
    counting array at index 5.

    4. Accumulate counts: Modify the counting array so that each element at index `i` contains the sum of all counts up
    to index `i`. This step allows you to determine the correct position of each element in the sorted output.

    5. Build the sorted array: Create an output array of the same size as the input array. For each element in the input
    array, look up its count in the counting array to determine its position in the output array. Decrease the count in
    the counting array to handle duplicate elements with the same value.

    6. Copy elements to the output array: Iterate through the input array again, place each element in its correct sorted
    position in the output array, and decrement the count in the counting array for that element.

 """


def counting_sort(arr):

    # Find the range of input values
    max_val = max(arr)

    # Create a counting array and initialize it
    counting_array = [0] * (max_val + 1)

    # Count occurrences of each element
    for num in arr:
        counting_array[num] += 1

    # Accumulate counts
    for i in range(1, len(counting_array)):
        counting_array[i] += counting_array[i - 1]

    # Build the sorted array
    sorted_array = [0] * len(arr)
    for num in arr:
        sorted_array[counting_array[num] - 1] = num
        counting_array[num] -= 1

    return sorted_array


arr = [2,4,1,7,2,1,1]
print(counting_sort(arr))

"""
When we use counting sort ?
    1. Limited Range of Input Values: Counting Sort is most effective when the range of input values (the difference 
    between the maximum and minimum values) is not significantly larger than the number of elements to be sorted. 
    It is especially useful when the range of values is relatively small compared to the number of elements.
    
    2. Integer Values: Counting Sort is designed for sorting integer values. It's not suitable for sorting data with 
    complex comparison operations (like strings).
    
    3. No Negative Values: Counting Sort typically assumes that all input values are non-negative. To handle negative 
    values, you may need to perform some preprocessing or consider an extended version of Counting Sort.
    
    4. Stable Sorting: Counting Sort is a stable sorting algorithm, which means that it maintains the relative order of 
    equal elements. This property is useful in certain situations where you want to preserve the original order of equal 
    elements.
    
    5. Linear Time Complexity: Counting Sort has a linear time complexity, O(n + k), where 'n' is the number of elements
     to be sorted and 'k' is the range of input values. This makes it very efficient for sorting large datasets with a 
     limited range of values.
"""