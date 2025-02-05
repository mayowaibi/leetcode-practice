class Solution:
    # TC: O(n), SC: O(1)
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        indexes = []  # O(1) space because it never has more than 2 elements

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                indexes.append(i)
            # if there are more than 2 differences, it's automatically false
            if len(indexes) > 2:
                return False
        
        if len(indexes) == 2:
            i, j = indexes[0], indexes[1]
            return s1[i] == s2[j] and s1[j] == s2[i]
        
        # only return true if strings were originally equal
        return len(indexes) == 0
