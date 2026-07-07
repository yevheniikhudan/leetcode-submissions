class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList = defaultdict(list)
        for src, dst in sorted(tickets)[::-1]:
            adjList[src].append(dst)

        res = []

        def dfs(src):
            while adjList[src]:
                dst = adjList[src].pop()
                dfs(dst)

            res.append(src)

        dfs("JFK")
        return res[::-1]  