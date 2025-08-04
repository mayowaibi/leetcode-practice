class Solution:
    # Iterative DP Solution (Bottom-Up) - TC: O(n), SC: O(1)
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    # Memoized Solution (Top-Down) - TC: O(n), SC: O(n)
    def fib2(self, n: int) -> int:
        memo = {}  # "cache" to store previously computed results

        def helper(k):
            if k == 0: return 0
            if k == 1: return 1
            if k in memo:
                return memo[k]
            
            memo[k] = helper(k - 1) + helper(k - 2)
            return memo[k]

        return helper(n)

    # Basic Recursive Solution - TC: O(2^n) SC: O(n) 
    def fib3(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        return self.fib(n-1) + self.fib(n-2)