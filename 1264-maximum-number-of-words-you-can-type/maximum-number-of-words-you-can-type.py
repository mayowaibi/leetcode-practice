class Solution:
    # TC: O(n), SC: O(n) where is the number of words in text
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        res = 0

        for word in words:
            valid = True
            for c in brokenLetters:
                if c in word:
                    valid = False
                    break
            if valid:
                res += 1
        
        return res