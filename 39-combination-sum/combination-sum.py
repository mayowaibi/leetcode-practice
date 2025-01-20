class Solution:
    # Recursive Backtracking Solution - TC: O(2^t), SC: O(t/d) where t is the target
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        # backtrack here is a form of dfs
        def backtrack(i: int, currList: List[int], total: int):
            # add a copy of currList to res if total matches the target
            # important to add copy because list is being modified in backtracking calls
            if total == target:
                res.append(currList.copy())
                return
            # if out of bounds or total passes target, stop backtracking
            if i == len(candidates) or total > target:
                return
            
            # recursive call 1 (first path in decision tree)
            currList.append(candidates[i])
            backtrack(i, currList, total + candidates[i])
            # backtracking - remove last el. in list to reset for other combinations
            currList.pop()
            # recursive call 2 (second path in decision tree)
            backtrack(i + 1, currList, total)

        backtrack(0, [], 0)

        return res