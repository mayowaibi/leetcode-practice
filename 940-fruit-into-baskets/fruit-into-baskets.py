class Solution:
    # Sliding Window + Hashmap Solution - TC: O(n), SC: O(1)
    def totalFruit(self, fruits: List[int]) -> int:
        fruit_map = defaultdict(int)

        l = 0
        for r in range(len(fruits)):
            fruit_map[fruits[r]] += 1

            if len(fruit_map) > 2:
                # remove the leftmost element from the map
                fruit_map[fruits[l]] -= 1
                if fruit_map[fruits[l]] == 0:
                    fruit_map.pop(fruits[l])
                l += 1

        return r - l + 1

    # Brute Force Solution - TC: O(n^2), SC: O(1)
    def totalFruit2(self, fruits: List[int]) -> int:
        res = 0

        for i in range(len(fruits)):
            unique = set()
            count = 0
            for j in range(i, len(fruits)):
                if fruits[j] not in unique and len(unique) == 2:
                    break
                unique.add(fruits[j])
                count += 1
            res = max(res, count)
        
        return res 