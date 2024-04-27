class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        string1, string2 = "", ""

        for s in word1:
            for c in s:
                string1 += c

        for s in word2:
            for c in s:
                string2 += c
        
        return string1 == string2