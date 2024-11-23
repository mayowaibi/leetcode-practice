class Solution:
    # Heap Solution - TC: O(nlogk) - heap rearrangement (logk) is done n times, SC: O(k)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for num in nums:
            # fill up the heap
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                # remove elements from the heap if they aren't in k largest
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
        
        return heap[0]

    # Sorting Solution - TC: O(nlogn), SC: O(1)
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]