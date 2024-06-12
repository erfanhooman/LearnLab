"""
Bucket Sort is a non-comparative sorting algorithm that distributes elements from an input array into a finite number of
buckets and then sorts each bucket individually, typically using a different sorting algorithm or recursively applying
Bucket Sort. It is particularly efficient when the input data is uniformly distributed across a range of values,
and the number of elements in each bucket is manageable.

Here's the Bucket Sort algorithm in a step-by-step explanation:

1. Determine the range of input values and divide it into a set of equally spaced buckets. The number of buckets is
typically determined by the range of values and the desired distribution of elements in each bucket.

2. Traverse the input array and place each element into the appropriate bucket based on its value. This can be done
using a simple mapping function. Elements within each bucket do not need to be sorted relative to each other at this
point.

3. Sort each individual bucket. The sorting method used for each bucket can vary. Commonly used sorting algorithms for
this step include Insertion Sort, Quick Sort, or even another recursive call to Bucket Sort.

4. Concatenate the sorted buckets to form the final sorted array. The order in which the buckets are combined is
determined by the ordering of the bucket values.
"""


def bucket_sort(arr):
    # Find the range of input values
    min_val, max_val = min(arr), max(arr)

    # Determine the number of buckets
    num_buckets = len(arr)

    # Create the buckets
    buckets = [[] for _ in range(num_buckets)]

    # Place elements into the buckets
    for num in arr:
        index = (num - min_val) * (num_buckets - 1) // (max_val - min_val)
        buckets[index].append(num)

    # Sort each bucket (Insertion Sort is used here)
    for i in range(num_buckets):
        buckets[i].sort()

    # Concatenate the sorted buckets to form the final sorted array
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


"""
When we use Bucket sort ? 
    1. Uniformly Distributed Data: Bucket sort is most effective when the input data is uniformly distributed across 
    a range. In such cases, the elements are evenly spread out, which makes it possible to divide the range into multiple 
    buckets.
    
    2. Known Range of Values: Bucket sort is suitable when you know the range of values that the input can take. 
    This allows you to predefine the range and create buckets accordingly.
    
    3. Close to Uniform Distribution: Even if the data is not perfectly uniformly distributed, bucket sort can still 
    work well if the distribution is reasonably close to uniform. It can handle some variability in the data.
    
    4. External Sorting: Bucket sort can be useful for external sorting, where data is too large to fit in memory.
    It can be used as a preliminary step in the sorting process before merging sorted sublists.
    
    6. Parallel Processing: In parallel computing environments, bucket sort can be an efficient choice as the individual
        buckets can be sorted independently on separate processors.
    
    """