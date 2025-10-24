class Solution:
    # Sorting + Two Pointers Solution - TC: O(nlogn), SC: O(1)
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        res = 0

        l, r = 0, len(skill) - 1
        pair_sum = skill[l] + skill[r]
        while l < r:
            if skill[l] + skill[r] != pair_sum:
                return -1

            res += skill[l] * skill[r]
            l += 1
            r -= 1

        return res        
