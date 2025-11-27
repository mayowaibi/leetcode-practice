class Solution:
    # Sliding Window + Hashmap Solution
    # TC: O(len(s2)), SC: O(26) = O(1)
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_counter = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])

        if s1_counter == s2_counter:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            s2_counter[s2[l]] -= 1
            s2_counter[s2[r]] = 1 + s2_counter.get(s2[r], 0)

            if s2_counter[s2[l]] == 0:
                del s2_counter[s2[l]]
            
            l += 1

            if s1_counter == s2_counter:
                return True
        
        return False