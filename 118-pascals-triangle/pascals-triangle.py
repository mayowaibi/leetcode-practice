class Solution:
    # Iterative "DP" Solution - TC: O(n^2), SC: O(1) not counting output
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(2, numRows+1):
            prev_row = res[-1]
            # first value is always 1
            new_row = [1]

            # add the middle numbers
            for j in range(1, i-1):
                new_row.append(prev_row[j-1] + prev_row[j])

            # last value is always 1
            new_row.append(1)

            res.append(new_row)
            
        return res

    # Inefficient Recursive Solution - TC: O(n^3), SC: O(n^2)
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