class Solution:
    # Hashmap + String Traversal Solution - TC: O(n), SC: O(n)
    def firstUniqChar(self, s: str) -> int:
        # Fill hashmap with characters and their occurences
        hashmap = Counter(s)

        # Re-iterate through string to find first unique character, if it exists
        for i, c in enumerate(s):
            if hashmap[c] == 1:
                return i

        return -1