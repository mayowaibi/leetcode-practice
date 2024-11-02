class Solution:
    # Hashmap + Mod Solution - TC: O(n), SC: O(1) [0, 23]
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        hour_map = defaultdict(int)     # remainder : no of occurrences
        res = 0

        for h in hours:
            remainder = h % 24
            # target is any number that can pair with current t
            target = 0 if remainder == 0 else 24-remainder
            # add target count to result
            res += hour_map[target]
            # update current h's remainder count to map
            hour_map[remainder] += 1

        return res