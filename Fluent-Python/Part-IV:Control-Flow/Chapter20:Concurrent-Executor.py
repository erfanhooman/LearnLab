"""
What is the futures
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import time

"""
Using concurrent.futures.as_completed is an excellent approach to handle futures as they complete, regardless of the 
order in which they were submitted. This method returns an iterator that yields futures as they complete, allowing you
 to process results or handle exceptions as soon as any future is done.
 if you don't use future.as_completed:
 
When you call future.result(), it blocks until the future is done. This means:

If the future is already completed, it returns the result immediately.
If the future is not yet completed, it waits (blocks) until the future is completed before returning the result.
"""


def task(n):
    if n == 3:
        raise ValueError("An error occurred in task 3")
    print(f"Starting task {n}")
    time.sleep(2)
    print(f"Task {n} completed")
    return n * 2


# Create a ThreadPoolExecutor with 3 worker threads
with ThreadPoolExecutor(max_workers=3) as executor:
    futures = [executor.submit(task, i) for i in range(5)]

    for future in as_completed(futures):
        try:
            result = future.result()
            print(f"Result: {result}")
        except Exception as e:
            print(f"Task raised an exception: {e}")
