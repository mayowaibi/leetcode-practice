class Solution:
    # Merge Sort Solution - TC: O(nlogn), SC: O(n)
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums

    def merge(self, array: List[int], left: int, mid: int, right: int) -> None:
        n = mid - left + 1
        m = right - mid

        L = array[left:left + n]
        R = array[mid + 1:mid + 1 + m]

        i = 0
        j = 0
        k = left

        while i < n and j < m:
            if L[i] <= R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            
            k += 1

        while i < n:
            array[k] = L[i]
            i += 1
            k += 1

        while j < m:
            array[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, array: List[int], left: int, right: int) -> None:
        if left < right:
            mid = (left + right) // 2

            self.mergeSort(array, left, mid)
            self.mergeSort(array, mid + 1, right)

            self.merge(array, left, mid, right)