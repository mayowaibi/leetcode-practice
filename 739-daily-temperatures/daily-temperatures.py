class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)    # output array initialized with 0s
        stack = []

        for r in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[r]:
                l = stack.pop()
                result[l] = r-l
            stack.append(r)
        
        return result