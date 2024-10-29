class Solution:
    # Three Pointer Solution - TC: O(n), SC: O(1)
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        ans, odd_count = 0, 0
        l, m = 0, 0

        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                odd_count += 1

            # reduce odd numbers from subarray until their count matches k
            while odd_count > k:
                if nums[l] % 2 == 1:
                    odd_count -= 1
                l += 1
                m = l

            if odd_count == k:
                # shift mid pointer to position of first odd element in subarray
                while nums[m] % 2 == 0:
                    m += 1
                ans += (m-l) + 1  # to account for 0-based indices

        return ans