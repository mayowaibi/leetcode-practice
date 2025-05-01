class Solution:
    # Two-Pointer Monotonic Stack Solution - TC: O(n),  SC: O(n)
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)    # output array initialized with 0s
        stack = []  # storing indices of temperatures

        for r in range(len(temperatures)):

            # while the current temp is higher than the last stored index's temp from stack
            while stack and temperatures[stack[-1]] < temperatures[r]:
                l = stack.pop()  # get the index with the lower temp
                result[l] = r-l  # calculate number of days until warmer temp

            stack.append(r)  # add current index to the stack
        
        return result