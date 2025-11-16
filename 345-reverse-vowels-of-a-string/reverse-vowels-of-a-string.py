class Solution:
    # TC: O(n), SC: O(n)
    def reverseVowels(self, s: str) -> str:
        # store set of all vowels (upper and lower case)
        all_vowels = {'a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U'}

        # itr through s and store all vowels in order in a list
        vowel_list = []
        for c in s:
            if c in all_vowels:
                vowel_list.append(c)

        # build a new list (to become str later) by copying elements from s 
        # but replacing vowels with vowels from vowel_list in reverse order
        output_list = []
        vowel_list_idx = len(vowel_list) - 1
        for c in s:
            if c in all_vowels:
                output_list.append(vowel_list[vowel_list_idx])
                vowel_list_idx -= 1
            else:
                output_list.append(c)

        # convert final list to string and return
        return ''.join(output_list)