class Solution:
    # Counter Solution - TC: O(n+m), SC: O(n)
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Simply check if both lists are permutations of each other
        return Counter(target) == Counter(arr)