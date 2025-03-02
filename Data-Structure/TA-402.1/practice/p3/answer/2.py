def bucket_sort_string(s):
    # Create 26 buckets for each letter of the alphabet
    buckets = [[] for _ in range(26)]

    # Place characters into the appropriate bucket
    for char in s:
        index = ord(char.lower()) - ord('a')  # Find the bucket index

        buckets[index].append(char)

    # Concatenate buckets into a sorted string

    sorted_string = []
    for bucket in buckets:
        bucket.sort()
        sorted_string.extend(bucket)

    return sorted_string


# Example usage
input_string = "bucketSortAlgorithm"
sorted_string = bucket_sort_string(input_string)
print(f"Original String: {input_string}")
print(f"Sorted String: {sorted_string}")