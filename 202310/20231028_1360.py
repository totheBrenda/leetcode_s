## https://leetcode.com/problems/number-of-days-between-two-dates/

from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date1 = datetime.strptime(date1, '%Y-%m-%d')
        date2 = datetime.strptime(date2, '%Y-%m-%d')
        return abs((date1-date2).days)