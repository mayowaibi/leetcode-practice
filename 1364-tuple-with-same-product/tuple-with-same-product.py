class Solution:
    # Hashmap (+ Math) Solution - TC: O(n^2), SC: O(n^2)
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = 0
        product_count = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                res += 8 * product_count[product]
                product_count[product] += 1
        
        return res