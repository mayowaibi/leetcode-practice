class Solution:
    # Sorting and Greedy Approach - TC: O(n), SC: O(nlogn)
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        count = Counter(hand)
        sorted_keys = sorted(count.keys())

        for key in sorted_keys:
            if count[key] > 0:
                start_count = count[key]
                for i in range(key, key + groupSize):
                    if count[i] < start_count:
                        return False
                    count[i] -= start_count
        return True