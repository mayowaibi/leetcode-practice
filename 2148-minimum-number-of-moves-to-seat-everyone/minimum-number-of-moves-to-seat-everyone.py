class Solution:
    # Sorting Solution - TC: O(n logn), SC: O(n)
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        result = 0

        for i in range(len(seats)):
            result += abs(seats[i] - students[i])
        
        return result