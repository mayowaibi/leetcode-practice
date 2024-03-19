class KthLargest:
    # TC: n log(n) because values could be popped up to (n-k) times
    # in the worst case and popping is a log(n) operation
    def __init__(self, k: int, nums: List[int]):
        # creating a minHeap to store the k largest integers
        # to ensure the heap's root is automatically the kth largest element
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # creating the heap has an O(n) TC
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    # TC: log(n)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)