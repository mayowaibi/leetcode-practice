class Solution:
    # Hashmap Solution - TC: O(n), SC: O(n)
    def maxFreqSum(self, s: str) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        max_vowel = max_consonant = 0
        letter_count = Counter(s)

        for c in s:
            if c in vowels:
                max_vowel = max(max_vowel, letter_count[c])
            else:
                max_consonant = max(max_consonant, letter_count[c])


        return max_vowel + max_consonant