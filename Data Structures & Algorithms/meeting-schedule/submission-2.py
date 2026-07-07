"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x.start)
        res = True

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return res