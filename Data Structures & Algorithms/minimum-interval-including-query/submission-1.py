class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # define interval size helper function
        # use heap to find the minimum interval
        intervals.sort(key=lambda x: x[0])

        res = {}
        i = 0
        heap = []
        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                heapq.heappush(heap, [self.intervalSize(intervals[i]), intervals[i][1]])
                i += 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)

            res[query] = heap[0][0] if heap else -1

        return [res[q] for q in queries]

    def intervalSize(self, interval):
        return interval[1] - interval[0] + 1