class Solution:
    # TC: O(n), SC: O(n) where n is the num of chars in sentence
    def isCircularSentence(self, sentence: str) -> bool:
        if sentence[0] != sentence[-1]:
            return False
    
        word_list = sentence.split(" ")
        
        if len(word_list) == 1:
            return True
            
        for i in range(1, len(word_list)):
            if word_list[i-1][-1] != word_list[i][0]:
                return False
        
        return True