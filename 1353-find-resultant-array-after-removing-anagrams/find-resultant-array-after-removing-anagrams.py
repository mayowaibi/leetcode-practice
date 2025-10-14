class Solution:
    # Hashmap Solution - TC: O(n*m), SC: O(m)
    # where n = num of words and m = avg len of all words
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        word1_counter = Counter(words[0])

        for i in range(1, len(words)):
            word2_counter = Counter(words[i])
            if word1_counter != word2_counter:
                res.append(words[i])
                word1_counter = word2_counter
        
        return res