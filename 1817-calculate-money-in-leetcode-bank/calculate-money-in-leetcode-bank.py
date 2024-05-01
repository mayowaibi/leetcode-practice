class Solution:
    # Basic Loop with Counter Variables - TC: O(n), SC: O(1)
    def totalMoney(self, n: int) -> int:
        result = 0
        # count is used to signal a new week, i is the value to be added to result
        count, i = 1, 1

        for x in range(n):
            result += i
            if i == 6 + count:
                count += 1
                i = count
            else:
                i += 1
        
        return result
            