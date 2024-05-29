class Solution:
    # Hashmap Solution: TC: O(n), SC: O(n)
    def findLucky(self, arr: List[int]) -> int:
        hashmap = Counter(arr)
        result = -1

        for num in hashmap:
            if hashmap[num] == num:
                result = max(result, num)

        return result