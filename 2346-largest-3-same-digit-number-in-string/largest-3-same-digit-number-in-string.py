class Solution:
    # TC: O(n), SC: O(1)
    def largestGoodInteger(self, num: str) -> str:
        res = ""
        max_good_int = -1

        for i in range(len(num) - 2):
            if num[i] == num[i+1] == num[i+2]:
                curr = num[i:i+3]
                curr_int = int(curr)
                if curr_int > max_good_int:
                    max_good_int = curr_int
                    res = curr
        
        return res