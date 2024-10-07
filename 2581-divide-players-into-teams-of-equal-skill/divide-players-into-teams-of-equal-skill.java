class Solution {
    // Sorting Solution - TC: O(nlogn), SC:O(1)
    public long dividePlayers(int[] skill) {
        Arrays.sort(skill);

        long res = 0;
        int l = 0, r = skill.length-1;
        int teamSum = skill[l] + skill[r];

        while (l < r) {
            if (teamSum != skill[l] + skill[r]) {
                return -1;
            }
            res += skill[l] * skill[r];
            l++;
            r--;
        }

        return res;
    }
    // Hashmap Solution - TC: O(n), SC: O(n)
    public long dividePlayers2(int[] skill) {
        int totalSum = Arrays.stream(skill).sum();

        if (totalSum * 2 % skill.length != 0) {
            return -1;
        }

        Map<Integer, Integer> count = new HashMap<>();
        for (int s : skill) {
            count.put(s, count.getOrDefault(s, 0) + 1);
        }

        long res = 0;
        int target = (totalSum * 2) / skill.length;

        for (int s : skill) {
            // // If s count is zero, no need to find a matching pair
            if (count.get(s) == 0) {
                continue;
            }
            
            int diff = target - s;
            // If diff count is zero or diff not in count,
            // no valid division can be made (no pair for s)
            if (!count.containsKey(diff) || count.get(diff) == 0) {
                return -1;
            }
            // else, add pair to sum and decrement diff count
            res += s * diff;
            count.put(s, count.get(s) - 1);
            count.put(diff, count.get(diff) - 1);
        }
        return res;
    }
}