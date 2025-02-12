class Solution:
    # Hashmap Solution - TC: O(n), SC: O(n)
    def maximumSum(self, nums: List[int]) -> int:
        digit_sums = {}  # key = sum of digits, value = largest num with the sum
        res = -1

        for num in nums:
            digit_sum = sum(int(d) for d in str(num))

            if digit_sum in digit_sums:
                curr_sum = digit_sums[digit_sum] + num
                res = max(res, curr_sum)
            
            digit_sums[digit_sum] = max(digit_sums.get(digit_sum, 0), num)

        return res

    # Brute Force Solution - TC: O(n^2), SC: O(1)
    def maximumSum2(self, nums: List[int]) -> int:
        res = -1

        for i in range(len(nums)):
            num1 = str(nums[i])
            num1sum = sum(int(d) for d in num1)

            for j in range(i+1, len(nums)):
                num2 = str(nums[j])
                num2sum = sum(int(d) for d in num2)
                
                if num1sum == num2sum:
                    res = max(res, nums[i]+nums[j])

        return res