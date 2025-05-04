class Solution:
    # Two-Pointer Solution - TC: O(n), SC: O(1)
    def compress(self, chars: List[str]) -> int:
        res = 0

        charCount = 1  # count the freq of occurences for the curr char
        l, r = 0, 0

        while r < len(chars):
            # check if we reached the end of the string or if the current character is different from the next
            if r == len(chars) - 1 or chars[r] != chars[r + 1]:
                # add curr char to res once the end of the group is reached
                res += 1
                chars[l] = chars[r]
                l += 1

                # only add the count if greater than 1
                if charCount > 1:
                    charCountStr = str(charCount)
                    res += len(charCountStr)

                    # add the digits of the count to the list
                    for c in charCountStr:
                        chars[l] = c
                        l += 1

                # reset the counter for the next group
                charCount = 1
            else:
                charCount += 1

            r += 1

        return res  # return the new length of the compressed list