class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        res, flag = 1, 1  # flag to represent what direction the line is going

        while time > 0:
            if flag == 1:
                res += 1
                if res == n:
                    flag = -1
            elif flag == -1:
                res -= 1
                if res == 1:
                    flag = 1
            time -= 1
            
        return res