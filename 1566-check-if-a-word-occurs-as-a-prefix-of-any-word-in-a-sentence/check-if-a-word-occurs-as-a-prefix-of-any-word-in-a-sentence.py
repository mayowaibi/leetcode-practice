class Solution:
    # Basic Traversal Solution - TC: O(n), SC: O(n)
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        sentence_list = sentence.split()
        
        for i, word in enumerate(sentence_list):
            if word.startswith(searchWord):
                return i + 1
        
        return -1