class Solution:
    # TC: O(nlogn), SC: O(n)
    def sortVowels(self, s: str) -> str:
        all_vowels = set("AEIOUaeiou")
        # create list of vowels in s and sort
        vowels = [c for c in s if c in all_vowels]
        vowels.sort()

        # create output list that replaces vowels in the order they
        # appear in vowel list and leaves consonants in the same position
        output_list = []
        vowel_idx = 0
        for c in s:
            if c in all_vowels:
                output_list.append(vowels[vowel_idx])
                vowel_idx += 1
            else:
                output_list.append(c)
        
        return ''.join(output_list)