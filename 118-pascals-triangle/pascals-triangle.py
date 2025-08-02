class Solution:
    # "Dynamic Programming Solution" - TC: O(n^2), SC: O(n^2)
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(2, numRows+1):
            res.append([1] + [res[-1][j] + res[-1][j+1] for j in range(i-2)] + [1])
        return res

    # Inefficient Recursive Solution - TC: O(n^3), SC: n^2
    def generate2(self, numRows: int) -> List[List[int]]:
        res = []
    
        def pascal(n):
            local_res = [0] * n
            local_res[0] = local_res[-1] = 1
            if n == 1 or n == 2:
                return local_res

            prev_list = pascal(n-1)
            for i in range(1, n-1):
                local_res[i] = prev_list[i-1] + prev_list[i]
            return local_res

        for n in range(1, numRows+1):
            res.append(pascal(n))

        return res