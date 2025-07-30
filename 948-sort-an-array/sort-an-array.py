class Solution:
    # TC: O(nlogn), SC: O(n) - All Solutions (Average Case)
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    # 1 - Merge Sort 
    def mergeSort(self, arr):
        n = len(arr)
        if n <= 1:
            return arr
        
        mid = n // 2
        L = arr[:mid]
        R = arr[mid:]

        L = self.mergeSort(L)
        R = self.mergeSort(R)

        return self.merge(L, R)
    
    # Merge - TC: O(n), SC: O(n)
    def merge(self, left, right):
        i = j = 0
        result = []

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])

        return result

    # 2 - Quick Sort
    def quickSort(self, arr):
        if len(arr) <= 1:
            return arr

        pivot = arr[-1]
        L = [v for v in arr[:-1] if v <= pivot]
        R = [v for v in arr[:-1] if v > pivot]

        L = self.quickSort(L)
        R = self.quickSort(R)

        return L + [pivot] + R

    # 3 - Heap Sort
    def heapSort(self, arr):
        n = len(nums)
        heapq.heapify(nums)
        result = []

        for _ in range(n):
            result.append(heapq.heappop(nums))

        return result