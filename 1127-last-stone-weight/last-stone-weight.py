class Solution:
    # Max-heap solution using a min-heap with negative values
    # TC: O(nlogn), SC: O(n)
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            # extracting the two heaviest stones
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)

            if stone1 != stone2:
                # adding the difference of the two stones to the heap
                heapq.heappush(stones, stone1 - stone2)
        
        # append 0 to the heap in case there are no stones left
        stones.append(0)
        # remove the negation before returning the final value
        return abs(stones[0])