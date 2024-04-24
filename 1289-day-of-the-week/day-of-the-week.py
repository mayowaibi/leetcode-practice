class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Using an in-built function
        return date(year, month, day).strftime("%A")