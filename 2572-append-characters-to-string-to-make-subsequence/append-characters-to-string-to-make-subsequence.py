class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointer1, pointer2 = 0, 0

        while pointer1 < len(s) and pointer2 < len(t):
            if s[pointer1] == t[pointer2]:
                pointer1 += 1
                pointer2 += 1
            else:
                pointer1 += 1
        
        return len(t) - pointer2