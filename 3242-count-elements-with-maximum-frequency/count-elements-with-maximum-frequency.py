class Solution:
    # Hashmap Solution - TC: O(3n), SC: O(n)
    def maxFrequencyElements(self, nums: List[int]) -> int:
        num_counter = Counter(nums)
        max_freq = 0
        res = 0

        for freq in num_counter.values():
            max_freq = max(max_freq, freq)
        
        for num in num_counter:
            if num_counter[num] == max_freq:
                res += max_freq
        
        return res