class Solution:
    def fairCandySwap(self, a: List[int], b: List[int]) -> List[int]:
        sum_a = sum(a)
        sum_b = sum(b)
        set_a = set(a)
        mean = (sum_a + sum_b) // 2
        
        # Search for candy box in b that satisfies fair swap.
        for count in b:
            # Get difference between the mean and bob's total candy minus the current box.
            difference = mean - sum_b + count
            
            # The difference isn't zero and alice has a candy box with an amount that matches this difference.
            if difference > 0 and difference in set_a:
                return [difference, count]
            
        # Should never get here. Return an empty list.
        return []