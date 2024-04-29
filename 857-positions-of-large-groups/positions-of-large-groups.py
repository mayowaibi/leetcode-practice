class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        result = []
        l = 0
        
        for i in range(len(s)):
            if s[i] == s[l]:
                continue
            
            if i - l >= 3:
                result.append([l, i - 1])
            
            l = i

        if i - l >= 2:
            result.append([l, i])
        
        return result