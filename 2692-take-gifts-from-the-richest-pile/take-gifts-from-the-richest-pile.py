class Solution:
    # Heap Solution - TC: O(k*logn + n), SC: O(n)
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts_heap = [-g for g in gifts]     # initialize with -ve elements for max-heap
        heapq.heapify(gifts_heap)    # O(n) each for this line and the one above 

        for _ in range(k):
            n = -1 * heapq.heappop(gifts_heap)   # negate num before taking its sqrt
            heapq.heappush(gifts_heap, -1 * floor(sqrt(n)))   # negate num before adding back to heap

        return -1 * sum(gifts_heap) # negate sum before returning

    # "Obtain Max" Solution - TC: O(k*n), SC: O(1)
    def pickGifts2(self, gifts: List[int], k: int) -> int:

        for _ in range(k):
            max_index = gifts.index(max(gifts)) # O(n)

            gifts[max_index] = math.floor(math.sqrt(gifts[max_index]))

        return sum(gifts)   # O(n)

    # Sorting Solution - TC: O(k*n*logn), SC: O(1)
    def pickGifts3(self, gifts: List[int], k: int) -> int:

        for _ in range(k):
            gifts.sort()    # O(n*logn)

            gifts[-1] = math.floor(math.sqrt(gifts[-1]))
        
        return sum(gifts)   # O(n)