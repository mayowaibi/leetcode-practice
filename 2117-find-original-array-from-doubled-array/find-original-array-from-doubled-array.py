class Solution:
    # Hashmap + Sorting Solution - TC: O(nlogn), SC: O(n)
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        res = []

        # arr len has to be even to be a valid doubled array
        if n % 2 == 1: return res

        counter = Counter(changed)
        changed.sort()

        for num in changed:
            # edge case
            # if 0 is in original array (0 count should be even)
            if num == 0 and counter[num] >= 2:
                counter[num] -= 2
                res.append(num)
            # general case
            # if num is in original array
            elif num > 0 and counter[num] and counter[num*2]:
                counter[num] -= 1
                counter[num*2] -= 1
                res.append(num)

        return res if len(res) == n // 2 else []