class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewelSet = set()

        for j in jewels:
            jewelSet.add(j)

        result = 0

        for s in stones:
            if s in jewelSet:
                result += 1

        return result