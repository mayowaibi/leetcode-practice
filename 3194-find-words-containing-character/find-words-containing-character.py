class Solution:
    # TC: O(n), SC: O(1) excluding res list
    # n = no. characters in all words combined
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []

        for i in range(len(words)):
            for c in words[i]:
                if c == x:
                    res.append(i)
                    break
        
        return res
                    