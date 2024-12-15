class Solution:
    # TC: O(n), SC: O(1)
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        increasing = False
        decreasing = False

        for i in range(len(arr) - 1):
            # nums cannot be equal
            if arr[i] == arr[i + 1]: 
                return False

            # increasing section
            if arr[i] < arr[i + 1]:
                # invalid if in decreasing is True
                if decreasing: 
                    return False
                increasing = True
            # decreasing section
            elif arr[i] > arr[i + 1]:
                decreasing = True
                # no need to check if incrasing is true

        # return True only if both were True throughout arr
        return increasing and decreasing