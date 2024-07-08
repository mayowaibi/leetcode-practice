class Solution:
    def sortSentence(self, s: str) -> str:
        # Splits the string to contain the number first,
        # then stores each modified word in the array
        arr = [i[-1] + i[:-1] for i in s.split()]
        
        arr.sort()

        res = ""
        for w in arr:
            res += w[1:] + " "

        # Return final string with last space removed
        return res[:-1]
            