class MaxHeap:
    def __init__(self):
        self.heap = [None]  # The heap is 1-indexed, so the first element is None

    def insert(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def delete_max(self):
        if len(self.heap) == 1:
            return None  # Heap is empty

        max_value = self.heap[1]

        # Move the last element to the root
        self.heap[1] = self.heap[-1]
        self.heap.pop()

        # Heapify down to maintain the max-heap property
        self._heapify_down(1)

        return max_value

    def _heapify_up(self, index):
        while index // 2 > 0:  # move until reach the root (root is on index 1)
            parent_index = index // 2  # we can calculate the parent index by divide it to 2
            if self.heap[index] > self.heap[parent_index]:
                # Swap if the current node is greater than its parent
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        while 2 * index < len(self.heap):  # move until we reach the leaf
            left_child_index = 2 * index  # formula to calculate the left child
            right_child_index = left_child_index + 1

            # Determine the index of the larger child
            if self.heap[right_child_index] > self.heap[left_child_index]:
                max_child_index = right_child_index
            else:
                max_child_index = left_child_index

            # Swap if the current node is smaller than the larger child
            if self.heap[index] < self.heap[max_child_index]:
                self.heap[index], self.heap[max_child_index] = self.heap[max_child_index], self.heap[index]
                index = max_child_index
            else:
                break
