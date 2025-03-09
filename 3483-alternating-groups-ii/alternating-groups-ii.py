class Solution:
    # Sliding Window Solution - TC: O(n+k), SC: O(1)
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)
        l = 0
        res = 0

        # iterate through entire arr plus k - 1 to account for circular arr
        for r in range(1, N + k - 1):
            # start new window if two adjacent colours aren't alternating
            if colors[r % N] == colors[(r - 1) % N]:
                l = r 

            window_size = r - l + 1
            # ensure window size is always at most size k
            if window_size > k:
                l += 1
                window_size -= 1

            # add valid windows to result   
            if window_size == k:
                res += 1 
        
        return res