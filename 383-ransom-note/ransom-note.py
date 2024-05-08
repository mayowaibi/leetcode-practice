class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict1, dict2 = Counter(ransomNote), Counter(magazine)

        for c in ransomNote:
            if dict1[c] > dict2[c]:
                return False
        
        return True