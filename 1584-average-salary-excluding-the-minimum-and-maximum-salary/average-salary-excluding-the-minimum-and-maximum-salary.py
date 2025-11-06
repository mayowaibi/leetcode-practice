class Solution:
    # TC: O(n), SC: O(1)
    def average(self, salary: List[int]) -> float:
        min_salary = max_salary = salary[0]

        for s in salary[1:]:
            min_salary = min(min_salary, s)
            max_salary = max(max_salary, s)
        
        total = 0
        for s in salary:
            if s != min_salary and s != max_salary:
                total += s

        return total/(len(salary)-2)