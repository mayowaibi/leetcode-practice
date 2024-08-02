class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        count = 0

        for i in range(len(word)):
            words = set()
            for j in range(i, len(word)):
                if word[j] in 'aeiou':
                    words.add(word[j])
                    if len(words) >= 5:
                        count += 1
                else:
                    break

        return count