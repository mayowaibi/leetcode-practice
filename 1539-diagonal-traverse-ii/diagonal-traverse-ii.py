class Solution:
    # Default Dict Solution - TC: O(n*m), SC: O(n*m)
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        diags = defaultdict(list)
        ROWS = len(nums)

        # populating dict from bottom to top because
        # diagonals are visited diagonally upwards from bottom
        for row in range(ROWS - 1, -1, -1):
            for col in range(len(nums[row])):
                diags[row+col].append(nums[row][col])

        output = []
        key = 0
        while key in diags:
            output += diags[key]
            key += 1
        
        return output