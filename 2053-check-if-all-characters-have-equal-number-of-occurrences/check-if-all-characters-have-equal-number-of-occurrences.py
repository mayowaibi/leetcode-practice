class Solution:
    # Basic String Traversal + Hashmap Solution - TC: O(n), SC:O(n)
    def areOccurrencesEqual(self, s: str) -> bool:
        hashmap = Counter(s)

        # Alternative to using Counter method
        # hashmap = dict()

        # for c in s:
        #     hashmap[c] = 1 + hashmap.get(c, 0)

        for c in s:
            # if any letter's occurrence in the hashmap doesn't match
            # the first value's occurence, automatically false
            if hashmap[c] != hashmap[s[0]]:
                return False

        return True