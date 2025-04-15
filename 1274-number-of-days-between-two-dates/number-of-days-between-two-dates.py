class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        s1 = date.fromisoformat(date1)
        s2 = date.fromisoformat(date2)

        res = abs(s1 - s2)

        return res.days
        