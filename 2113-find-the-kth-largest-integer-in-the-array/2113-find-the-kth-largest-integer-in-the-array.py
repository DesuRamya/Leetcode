class MaxHeap:
    def __init__(self):
        self.heap = []
    def insert(self, item):
        heapq.heappush(self.heap, -item) 
    def delete_top(self):
        if self.heap:
            return -heapq.heappop(self.heap) 
        else:
            return "Heap is empty"
    def peek(self):
        return -self.heap[0] if self.heap else "Heap is empty"
class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        pq=MaxHeap()
        for i in nums:
            pq.insert(int(i))
        while k>1:
            pq.delete_top()
            k-=1
        return str(pq.peek())