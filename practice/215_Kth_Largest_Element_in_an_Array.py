class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        minHeap: list[int] = []

        for num in nums:
            self.heap_push(minHeap, num * -1)
        for i in range(k - 1):
            self.heap_pop(minHeap)

        return self.heap_pop(minHeap) * -1

    def heap_push(self, heap, val):
        heap.append(val)
        current = len(heap) - 1
        while current > 0:
            parent = (current - 1) // 2
            if heap[current] < heap[parent]:
                heap[current], heap[parent] = heap[parent], heap[current]
                current = parent
            else:
                break

    def heap_pop(self, heap):
        if not heap:
            return None
        root_val = heap[0]
        last_val = heap.pop()
        if heap:
            heap[0] = last_val
            self.heapify(heap, len(heap), 0)

        return root_val

    def heapify(self, arr, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] < arr[smallest]:
            smallest = left

        if right < n and arr[right] < arr[smallest]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            self.heapify(arr, n, smallest)
