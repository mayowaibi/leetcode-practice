class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        count = 0
        flag = self.isSorted(nums)

        while not flag:
            min_adj_sum = float("inf")
            indices = [0] * 2
            for i in range(1, len(nums)):
                if nums[i-1] + nums[i] < min_adj_sum:
                    min_adj_sum = nums[i-1] + nums[i]
                    indices[0] = i-1
                    indices[1] = i
            
            new_nums = []
            for i in range(len(nums)):
                if i == indices[0]:
                    new_nums.append(min_adj_sum)
                elif i == indices[1]:
                    continue
                else:
                    new_nums.append(nums[i])
            
            count += 1
            nums = new_nums
            flag = self.isSorted(new_nums)
        
        return count
        
    def isSorted(self, nums) -> bool:
        for i in range(1, len(nums)):
            if nums[i-1] > nums[i]:
                return False
        return True

    