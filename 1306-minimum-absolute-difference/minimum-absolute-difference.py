class Solution:
    # Sorting Solution - TC: O(nlogn), SC: O(n)
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float("inf")
        res = []

        # find min absolute diff
        for i in range(len(arr) - 1):
            minDiff = min(minDiff, abs(arr[i] - arr[i+1]))

        # find all pairs with min absolute diff
        for i in range(len(arr) - 1):
            if abs(arr[i]-arr[i+1]) == minDiff:
                res.append([arr[i], arr[i+1]])
            
        return res
