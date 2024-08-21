class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        letters = ['b', 'a', 'l', 'o', 'n']
        counts = [0] * 5

        for i in range(5):
            counts[i] = text.count(letters[i])
        
        counts[2], counts[3] = counts[2] // 2, counts[3] // 2

        return min(counts)
