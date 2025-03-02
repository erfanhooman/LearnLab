"""
modify Bucket Sort to handle both positive and negative numbers
"""

"""
This is a standard bucket sort implementation for non-negative numbers 
"""


# Helper function to perform bucket sort on non-negative numbers
def bucket_sort_positive(arr):
    if not arr:
        return []

    # Find the maximum value in the array to determine bucket ranges
    max_value = max(arr)

    # Create a number of buckets proportional to the size of the array
    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    # Place each element in its respective bucket
    for num in arr:
        index = int(num * bucket_count / (max_value + 1))  # Normalize the index
        buckets[index].append(num)

    # Sort individual buckets and concatenate the result
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(sorted(bucket))

    return sorted_array


"""
Since the bucket sort only works naturally for positive numbers, we convert negative numbers to positive by taking their absolute values.
"""


# Helper function to perform bucket sort on non-positive numbers
def bucket_sort_negative(arr):
    if not arr:
        return []

    # Convert negative numbers to positive by taking the absolute value
    # This allows us to use the same bucket sort logic as for positive numbers
    abs_arr = [-num for num in arr]

    # Perform bucket sort on the positive version of the negative numbers
    sorted_abs_arr = bucket_sort_positive(abs_arr)

    # Revert the sorted numbers back to negative
    return [-num for num in reversed(sorted_abs_arr)]


# Main function to sort an array with both positive and negative numbers
def bucket_sort(arr):
    # Separate the array into negative and positive numbers
    negative_numbers = [num for num in arr if num < 0]
    positive_numbers = [num for num in arr if num >= 0]

    # Sort negative and positive numbers separately
    sorted_negatives = bucket_sort_negative(negative_numbers)
    sorted_positives = bucket_sort_positive(positive_numbers)

    # Concatenate the sorted negative numbers and positive numbers
    return sorted_negatives + sorted_positives
