class Solution:
    # Brute Force Solution - TC: O(n^2), SC: O(1)
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        n = len(fruits)
        allotted = 0

        for i in range(n):
            for j in range(n):
                if fruits[i] <= baskets[j]:
                    allotted += 1
                    baskets[j] = 0
                    break

        return n - allotted
                