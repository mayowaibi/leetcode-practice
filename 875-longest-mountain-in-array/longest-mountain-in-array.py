class Solution:
    # Two Pointer Solution - TC: O(n) - each element is processed at most twice, SC: O(1)
    def longestMountain(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return 0

        res = 0
        i = 1
        
        # start from second element, end at second to last
        while i < len(arr) - 1:
            # Check if arr[i] is a peak in arr
            if arr[i - 1] < arr[i] > arr[i + 1]:
                # expand to the left
                left = i - 1
                while left > 0 and arr[left - 1] < arr[left]:
                    left -= 1

                # expand to the right
                right = i + 1
                while right < len(arr) - 1 and arr[right] > arr[right + 1]:
                    right += 1

                # calculate mountain length
                curr_length = right - left + 1
                res = max(res, curr_length)

                # move i to the end of the current mountain
                # this step ensures the algo has O(n) runtime
                i = right
            else:
                # skip i if it's not a peak
                i += 1

        return res