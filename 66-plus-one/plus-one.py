class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # reverse the list for easier traversal
        digits = digits[::-1]
        # carry: digit to be carried over, i: current index in loop
        carry, i = 1, 0

        # assume there is a 1 to be carried over each place value and 
        # continue loop until there is no carry over 1
        while carry == 1:
            # ensure that each digit is modified only if the index is within the length of digits
            if i < len(digits):
                # if current digit is 9, change to 0 and carry the 1 over
                if digits[i] == 9:
                    digits[i] = 0
                # if current digit is not 9, simply increment and do not carry over
                else:
                    digits[i] += 1
                    carry = 0
            # if index is larger than the length of digits, add a new digit to digits
            # and remove carry over 1 
            else:
                digits.append(1)
                carry = 0
            i += 1
        # re-reverse list before returning
        return digits[::-1]