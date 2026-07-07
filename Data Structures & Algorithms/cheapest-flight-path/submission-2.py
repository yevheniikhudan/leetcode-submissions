class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        adjList = [[] for _ in range(n)]
        for u, v, cst in flights:
            adjList[u].append([v, cst])

        q = deque([(0, src, 0)])

        while q:
            cst, node, stops = q.popleft()
            if stops > k:
                continue

            for adj, adjCost in adjList[node]:
                newCost = cst + adjCost
                if newCost < prices[adj]:
                    prices[adj] = newCost
                    q.append((newCost, adj, stops + 1))

        return prices[dst] if prices[dst] != float('inf') else -1