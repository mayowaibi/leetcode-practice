class Solution:
    # Counter Solution - TC: O(n), SC: O(n)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = Counter(nums)

        res = []
        # add k largest freqs to res and pop from hashmap after each iteration
        for i in range(k):
            curr_max = max(num_counter, key=num_counter.get)
            res.append(curr_max)
            num_counter.pop(curr_max)
        
        return res

    # Sorting Solution - TC: O(nlogn), SC: O(n)
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        unique_count = 1
        res = [nums[0]]

        for i in range(1, len(nums)):
            res.append(nums[i])
            if nums[i] != nums[i-1]:
                unique_count += 1
                if unique_count == k:
                    break
            
        return list(set(res))