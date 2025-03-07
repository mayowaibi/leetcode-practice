class Solution:
    # TC: O(n^2*m) where n = # words, m = avg # chars
    # SC: O(1) excl res
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for word1 in words:
            for word2 in words:
                if word1 != word2:
                    if word1 in word2 and word1 not in res:
                        res.append(word1)
                        break
                    if word2 in word1 and word2 not in res:
                        res.append(word2)

        return res