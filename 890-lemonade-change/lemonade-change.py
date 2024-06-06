class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fiveCount, tenCount = 0, 0

        for bill in bills:
            # If we get $5
            if bill == 5:
                fiveCount += 1
            # If we get $10
            elif bill == 10:
                if fiveCount >= 1:
                    fiveCount -= 1
                    tenCount += 1
                else:
                    return False
            # If we get $20
            else:
                if tenCount >= 1 and fiveCount >= 1:
                    tenCount -= 1
                    fiveCount -= 1
                elif fiveCount >= 3:
                    fiveCount -= 3
                else:
                    return False

        return True