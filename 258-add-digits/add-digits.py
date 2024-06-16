class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            numString = str(num)
            num = 0
            for i in range(len(numString)):
                num += int(numString[i])
        return num