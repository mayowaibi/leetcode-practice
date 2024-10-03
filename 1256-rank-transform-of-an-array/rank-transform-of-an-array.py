class Solution:
    # Sorting and Hashing Solution - TC: O(nlogn), SC: O(n)
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        value_to_rank = {}  # Dictionary to store value-to-rank mapping
        sorted_list = sorted(list(set(arr)))  # Remove duplicates and sort unique elements
        
        # Assign ranks to sorted unique elements
        for index in range(len(sorted_list)): 
            value_to_rank[sorted_list[index]] = index + 1
          
        # Replace each element in the original array with its rank
        for index in range(len(arr)): 
            arr[index] = value_to_rank[arr[index]]

        return arr