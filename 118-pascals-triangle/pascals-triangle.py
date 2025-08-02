class Solution:
    # Recursive Solution - TC: O(n^3)
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for n in range(1, numRows+1):
            res.append(self.pascal(n))
        return res
    
    def pascal(self, n):
        res = [0] * n
        res[0] = res[-1] = 1
        if n == 1 or n == 2:
            return res

        prev_list = self.pascal(n-1)
        for i in range(1, n-1):
            res[i] = prev_list[i-1] + prev_list[i]
        return res