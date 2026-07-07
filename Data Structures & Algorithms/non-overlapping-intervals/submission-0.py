class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        last = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < last:
                res += 1
            else:
                last = intervals[i][1]

        return res