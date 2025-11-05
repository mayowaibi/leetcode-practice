class Solution: 
    # Set Solution - TC: O(n), SC: O(n)
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        numset = set()

        for num in nums:
            if num in numset:
                res.append(num)
                continue
            numset.add(num)
        
        return res