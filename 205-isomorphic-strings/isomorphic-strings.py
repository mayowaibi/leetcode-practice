class Solution:
    # Hashmap Solution - TC: O(n), SC: O(n)
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        
        for c1, c2 in zip(s, t):
            if c1 in hashmap and hashmap[c1] != c2:
                return False
            elif c1 not in hashmap and c2 in hashmap.values():
                return False
            elif c1 not in hashmap:
                hashmap[c1] = c2
        return True