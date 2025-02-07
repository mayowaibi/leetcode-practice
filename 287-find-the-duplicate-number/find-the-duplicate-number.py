class Solution:
    # Linked List (Floyd-Warshall Algo) Solution - TC: O(n), SC: O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

    # Negative Marking Solution - TC: O(n), SC: O(1)
    # involves modifying the array
    def findDuplicate2(self, nums: List[int]) -> int:
        for num in nums:
            idx = abs(num) - 1

            if nums[idx] < 0:
                return abs(num)
                
            nums[idx] *= -1

    # Hashmap Solution - TC: O(n), SC: O(n)
    def findDuplicate3(self, nums: List[int]) -> int:
        num_map = Counter(nums)

        for num in num_map:
            if num_map[num] > 1:
                return num