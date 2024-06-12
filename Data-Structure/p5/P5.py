class MinHeap:
    def __init__(self, arr):
        self.heap = arr
        self.size = len(arr)

    def min_heapify(self, i):
        smallest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < self.size and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < self.size and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)

    def build_heap(self):
        for i in range(self.size // 2 - 1, -1, -1):
            self.min_heapify(i)

    def heap_sort(self):
        sorted_result = []

        while self.heap:
            self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
            sorted_result.append(self.heap.pop())
            self.min_heapify(0)

        return sorted_result


if __name__ == "__main__":
    input_array = [5, 3, 8, 2, 7, 1, 4, 6]
    min_heap = MinHeap(input_array)

    min_heap.build_heap()
    sorted_result = min_heap.heap_sort()

    print("Sorted Result:", sorted_result)
