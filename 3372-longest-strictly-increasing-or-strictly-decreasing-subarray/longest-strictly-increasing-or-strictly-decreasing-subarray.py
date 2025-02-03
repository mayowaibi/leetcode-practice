class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longestinc, longestdec = 0, 0
        currleninc = 1

        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                currleninc += 1
            else:
                longestinc = max(longestinc, currleninc)
                currleninc = 1

        currlendec = 1
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                currlendec += 1
            else:
                longestdec = max(longestdec, currlendec)
                currlendec = 1
        
        longestinc = max(longestinc, currleninc)
        longestdec = max(longestdec, currlendec)

        return max(longestinc, longestdec)