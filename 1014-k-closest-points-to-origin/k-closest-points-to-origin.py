class Solution:
    # Min-heap Solution - TC: O(n + klogn), SC: O(n)
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        # O(n)
        for x, y in points:
            # calculate distance between point and origin
            dist = x**2 + y**2
            # by default, python uses the first value as key for heap
            minHeap.append([dist, x, y])

        # O(n)
        heapq.heapify(minHeap)

        res = []
        # O(k*logn)
        for i in range(k):
            dist, x, y = heapq.heappop(minHeap) # O(logn)
            res.append([x, y])

        return res

    # Sorting Solution - TC: O(n + nlogn), SC: O(n)
    def kClosest2(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []

        for x, y in points:
            dist = x**2 + y**2
            distances.append([dist, x, y])
        
        distances.sort()

        res = []
        for i in range(k):
            res.append([distances[i][1], distances[i][2]])
        
        return res
