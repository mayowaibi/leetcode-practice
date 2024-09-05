class Solution:
    # Shorter Solution - TC: O(n), SC: O(n)
    def isPalindrome(self, s: str) -> bool:
        new = ''

        for c in s:
            if c.isalnum():
                new += c.lower()
        return new == new[::-1]

    # Two Pointer Solution - TC: O(n), SC: O(n)
    def isPalindrome2(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        
        while l < r:
            # check if left and right pointers point to alphanumeric characters
            while l < r and not s[l].isalnum():
                l += 1
            while r > l and not s[r].isalnum():
                r -= 1

            # check if left and right pointers don't point to the same character
            if s[l].lower() != s[r].lower():
                return False
            # increment and decrement pointers after every iteration
            l, r = l + 1, r - 1
        return True
