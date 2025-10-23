class Solution:
    # Brute Force Solution - TC: O(n^2), SC: O(1)
    def hasSameDigits(self, s: str) -> bool:
        digits = [int(digit) for digit in s]

        while len(digits) > 2:
            new_digits = []
            for i in range(1, len(digits)):
                pair_sum = digits[i-1] + digits[i]
                new_digits.append(pair_sum % 10)
            digits = new_digits

        return digits[0] == digits[1]