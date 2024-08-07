class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        i, count = 0, 1

        while candies > 0:
            if i == len(res):
                i = 0
            
            if candies >= count:
                res[i] += count
                candies -= count
                count += 1
            else:
                res[i] += candies
                break
            
            i += 1

        return res
        
        return res
