class Solution:
    # Sliding Window Solution
    def countVowelSubstrings(self, word: str) -> int:
        count = 0

        for start in range(len(word)):
            temp = set()
            for end in range(start, len(word)):
                if word[end] in 'aeiou':
                    temp.add(word[end])
                    if len(temp) >= 5:
                        count += 1
                else:
                    break   # Stop as soon as a non-vowel character is found

        return count