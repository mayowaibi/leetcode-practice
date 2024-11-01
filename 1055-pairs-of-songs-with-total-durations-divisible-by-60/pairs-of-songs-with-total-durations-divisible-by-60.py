class Solution:
    # Hashmap + Mod Solution - TC: O(n), SC: O(1) [0, 59]
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        duration_map = defaultdict(int)     # to store counts of each t % 60
        res = 0

        for t in time:
            remainder = t % 60
            # target is any number that can pair with current t
            target = 0 if remainder == 0 else 60-remainder
            # add target count to result
            res += duration_map[target]
            # update current t's remainder count to map
            duration_map[remainder] += 1

        return res

    # Brute Force Solution - TC: O(n^2), SC: O(1)
    def numPairsDivisibleBy60V2(self, time: List[int]) -> int:
        res = 0

        for i in range(len(time)):
            for j in range(i+1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    res += 1

        return res