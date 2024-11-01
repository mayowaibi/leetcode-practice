class Solution:
    # Hashmap + Mod Solution - TC: O(n), SC: O(1) [0, 59]
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        duration_map = defaultdict(int)     # to store counts of each duration % 60
        res = 0

        for t in time:
            if t % 60 == 0:
                # increment res by the count of previous songs with remainder 0
                res += duration_map[0]
            else:
                # 60 - (t % 60) = number that can be added to t that would be a valid pair
                res += duration_map[60-(t % 60)]
            # add current t's remainder count to map
            duration_map[t % 60] += 1

        return res

    # Brute Force Solution - TC: O(n^2), SC: O(1)
    def numPairsDivisibleBy60V2(self, time: List[int]) -> int:
        res = 0

        for i in range(len(time)):
            for j in range(i+1, len(time)):
                if (time[i] + time[j]) % 60 == 0:
                    res += 1

        return res