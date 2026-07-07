class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        visited = [False] * n
        result = 0

        for src, dst in edges:
            adjList[src].append(dst)
            adjList[dst].append(src)

        def dfs(i, parent):
            if visited[i]:
                return

            visited[i] = True

            for adj in adjList[i]:
                if adj == parent:
                    continue

                dfs(adj, i)

        for i in range(n):
            if not visited[i]:
                result += 1
                dfs(i, -1)

        return result
