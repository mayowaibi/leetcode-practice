class Solution:
    # Boyer-Moore Voting Algorithm - TC: O(n), SC: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            # update count: increase if n == res, decrease otherwise
            count += (1 if res == n else -1)

        # at the end, res will contain the majority element
        return res

    # Hashmap Counter Solution - TC: O(n), SC: O(n)
    def majorityElement2(self, nums: List[int]) -> int:
        num_counter = Counter(nums)

        for n in num_counter:
            if num_counter[n] > floor(len(n)/2):
                return n