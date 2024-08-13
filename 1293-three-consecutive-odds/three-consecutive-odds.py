class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        i = 2

        while i < len(arr):
            if arr[i-2] % 2 == 1 and arr[i-1] % 2 == 1 and arr[i] % 2 == 1:
                return True
            i += 1
        
        return False