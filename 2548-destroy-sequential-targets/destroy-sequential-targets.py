class Solution:
    # Hashmap + Mod Solution - TC: O(n), SC: O(n)
    def destroyTargets(self, nums: List[int], space: int) -> int:
        # store frequencies of each target's remainder when divided by space
        target_map = defaultdict(int)   # remainder : no of occurrences

        # iterate through nums to populate map with counts
        for num in nums:
            target_map[num % space] += 1

        # save the target/remainder that appears the most
        max_freq = max(target_map.values())

        res = math.inf
        # iterate through nums again to find the min num who's rem maps to max_freq
        for num in nums:
            if target_map[num % space] == max_freq:
                res = min(res, num)

        return res