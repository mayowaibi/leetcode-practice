class Solution:
    # Greedy Hashmap Solution - TC: O(n), SC: O(n)
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        group_map = collections.defaultdict(list)
        res = []

        for i, size in enumerate(groupSizes):
            group_map[size].append(i)

            # reassign array for current size if full
            if len(group_map[size]) == size:
                res.append(group_map[size])
                group_map[size] = []

        return res