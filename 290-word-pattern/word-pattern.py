class Solution:
    # Hashmap Solution - TC: O(n), SC: O(n) where n is len(pattern)/len(words))
    def wordPattern(self, pattern: str, s: str) -> bool:
        wordToPattern = dict()
        words = s.split()

        # return false if pattern length != num of words
        if len(pattern) != len(words):
            return False
        # return false if num of unique letters in pattern != num of unique words
        if len(set(pattern)) != len(set(words)):
            return False

        # add every word to hashmap and map it to pattern
        # return false if word already has a mapping
        for i in range(len(words)):
            if words[i] not in wordToPattern:
                wordToPattern[words[i]] = pattern[i]
            elif wordToPattern[words[i]] != pattern[i]:
                return False

        return True