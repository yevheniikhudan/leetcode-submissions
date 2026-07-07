class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adjList = [[] for _ in range(n)]

        for src, dest in edges:
            adjList[src].append(dest)
            adjList[dest].append(src)

        visited = set()

        q = deque()
        q.append((0, -1))
        visited.add(0)

        while q:
            node, parent = q.popleft()

            for adj in adjList[node]:
                if adj == parent:
                    continue

                if adj in visited:
                    return False

                visited.add(adj)
                q.append((adj, node))

        return len(visited) == n