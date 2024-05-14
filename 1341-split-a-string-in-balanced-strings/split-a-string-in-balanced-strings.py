class Solution:
    def balancedStringSplit(self, s: str) -> int:

        lcount = 0
        rcount = 0
        result = 0

        for c in s:
            if c == 'L':
                lcount += 1
            else:
                rcount += 1
                
            if (lcount == rcount):
                result += 1
        
        return result