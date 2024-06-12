class MaxPriorityQueue:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.heap = []
        self.current_size = 0

    def is_empty(self):
        return self.current_size == 0

    def is_full(self):
        return self.current_size == self.max_capacity

    def enqueue(self, task, priority):
        if self.is_full():
            print("Priority queue is full. Cannot insert task:", task)
            return
        new_node = (task, priority)
        self.heap.append(new_node)
        self.current_size += 1
        self._up_heapify(self.current_size - 1)

    def peek_highest_priority_task(self):
        if self.is_empty():
            print("Priority queue is empty.")
            return None
        return self.heap[0][0]

    def dequeue_highest_priority_task(self):
        if self.is_empty():
            print("Priority queue is empty. Cannot dequeue highest priority task.")
            return None
        highest_priority_task = self.heap[0][0]
        last_node = self.heap.pop()
        self.current_size -= 1
        if self.current_size > 0:
            self.heap[0] = last_node
            self._down_heapify(0)
        return highest_priority_task

    def get_size(self):
        return self.current_size

    def _up_heapify(self, child_index):
        if child_index <= 0:
            return
        parent_index = (child_index - 1) // 2
        if self.heap[parent_index][1] < self.heap[child_index][1]:
            self.heap[parent_index], self.heap[child_index] = self.heap[child_index], self.heap[parent_index]
            self._up_heapify(parent_index)

    def _down_heapify(self, parent_index):
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2
        largest = parent_index

        if left_child_index < self.current_size and self.heap[left_child_index][1] > self.heap[largest][1]:
            largest = left_child_index
        if right_child_index < self.current_size and self.heap[right_child_index][1] > self.heap[largest][1]:
            largest = right_child_index

        if largest != parent_index:
            self.heap[parent_index], self.heap[largest] = self.heap[largest], self.heap[parent_index]
            self._down_heapify(largest)