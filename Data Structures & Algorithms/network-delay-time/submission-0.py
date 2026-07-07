class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjList = [[] for _ in range(n)]
        for u, v, w in times:
            adjList[u - 1].append([v, w])

        time = 0
        h = []
        heapq.heappush(h, [0, k])
        visit = set()

        while h:
            w, u = heapq.heappop(h)

            if u in visit:
                continue
            time = w
            visit.add(u)

            for v, w1 in adjList[u - 1]:
                if v in visit:
                    continue

                heapq.heappush(h, [w + w1, v])

        return time if len(visit) == n else -1