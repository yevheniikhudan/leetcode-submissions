class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, node = len(points), 0
        if n == 1:
            return 0

        dist = [float("inf")] * n
        visit = [False] * n
        numEdges, res = 0, 0

        while numEdges < n - 1:
            visit[node] = True
            nextNode = -1
            for i in range(n):
                if visit[i]:
                    continue
                curDist = abs(points[i][0] - points[node][0]) + abs(
                    points[i][1] - points[node][1]
                )
                dist[i] = min(dist[i], curDist)
                if nextNode == -1 or dist[i] < dist[nextNode]:
                    nextNode = i

            res += dist[nextNode]
            node = nextNode
            numEdges += 1

        return res