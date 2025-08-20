class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 2:
            n = n / 4
            
        return n == 1