class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(list)

        for u, v in edges:
            adjList[u].append(v)

        topSort = []
        visited = set()
        visiting = set()

        def dfs(i: int) -> bool:
            if i in visited:
                return True
            if i in visiting:
                return False

            visiting.add(i)

            for adj in adjList[i]:
                if not dfs(adj):
                    return False

            visiting.remove(i)
            visited.add(i)
            topSort.append(i)

            return True

        for i in range(n):
            if not dfs(i):
                return []

        topSort.reverse()
        return topSort