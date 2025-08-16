class Solution:
    # Brute Force Solution - TC: O(n), SC: O(n)
    def maximum69Number (self, num: int) -> int:
        num_str = str(num)
        res = []
        i = 0

        while i < len(num_str):
            if num_str[i] == '9':
                res.append(num_str[i])
                i += 1
            else:
                # simply change the first 6 to a 9
                res.append('9')
                i += 1
                break
        
        
        # add all the remaining characters if any
        res.append(num_str[i:])

        return int(''.join(res))
            

