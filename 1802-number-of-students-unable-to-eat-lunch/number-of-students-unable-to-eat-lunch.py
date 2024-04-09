class Solution:
    # HashMap Solution - TC: O(n), SC: O(1)
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        result = len(students)
        # Counter method counts every occurrence of each number and maps it into a hashmap
        count = Counter(students)
        
        # COUNTER METHOD IN LOOP FORM
        # count = {}
        # for s in students:
        #     if s not in count:
        #         count[s] = 0
        #     count[s] += 1
        
        for s in sandwiches:
            # if there is a student that wants the available sandwich
            if count[s] > 0:
                count[s] -= 1
                result -= 1
            # if there is no student that wants the available sandwich
            else:
                return result
            
        return result