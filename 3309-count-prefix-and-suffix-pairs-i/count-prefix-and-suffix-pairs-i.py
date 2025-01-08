class Solution:
    # Brute Force Solution (Nested Loop) - TC: O(n^2), SC: O(1)
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        def isPrefixAndSuffix(str1: str, str2: str):
            n1, n2 = len(str1), len(str2)

            if n1 > n2:  
                return False

            return str1 == str2[:n1] and str1 == str2[-n1:]
        
        res = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    res += 1
        
        return res