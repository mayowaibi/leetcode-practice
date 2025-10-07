class Solution:
    # TC: O(n), SC: O(1) excluding output list
    def sumZero(self, n: int) -> List[int]:
        res = []
        num = 1

        # if n is odd, add 0
        if n % 2 == 1:
            res.append(0)

        # add numbers symmetrically until list size == n
        while len(res) < n:
            res.append(num)
            res.append(-num)
            num += 1
            
        return res