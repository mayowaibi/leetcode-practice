class Solution:
    # TC: O(n+m) where n = len(nums) and m = len(queries), SC: O(n) 
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:  
        occ, ans = [], []

        for i, num in enumerate(nums):
            if num == x: 
                occ.append(i)
 
        for q in queries:
            if len(occ) < q: ans.append(-1)
            else: ans.append(occ[q-1])

        return ans