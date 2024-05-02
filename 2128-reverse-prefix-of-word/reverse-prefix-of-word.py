class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        index = -1

        for i,c in enumerate(word):
            if c == ch:
                index = i
                break
        
        if index == -1:
            return word
        else:
            prefix = word[:index+1]
            return prefix[::-1] + word[index+1:]