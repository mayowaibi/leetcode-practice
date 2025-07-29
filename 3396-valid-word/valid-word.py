class Solution:
    # Vowel Set Solution - TC: O(n), SC: O(1)
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowels = consonants = 0
        all_vowels = set("aeiouAEIOU")

        for c in word:
            if c.isalpha():
                if c in all_vowels:
                    vowels += 1
                else:
                    consonants += 1
            elif not c.isdigit():
                return False
        
        return vowels > 0 and consonants > 0