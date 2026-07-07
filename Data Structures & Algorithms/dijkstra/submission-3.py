class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adjList = [[] for _ in range(n)]
        shortest = {}

        for srcVertex, dstVertex, weight in edges:
            adjList[srcVertex].append([dstVertex, weight])

        h = []
        heapq.heappush(h, (0, src))

        while h:
            weight, vertex = heapq.heappop(h)

            if vertex in shortest:
                continue

            shortest[vertex] = weight

            for adjVertex, adjWeight in adjList[vertex]:
                if adjVertex in shortest:
                    continue

                heapq.heappush(h, (weight + adjWeight, adjVertex))

        for i in range(n):
            if i in shortest:
                continue

            shortest[i] = -1

        return shortest
                
