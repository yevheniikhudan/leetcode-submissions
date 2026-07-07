class DSU:
    def __init__(self):
        self.parent = {}
        self.rank = defaultdict(int)

    def find(self, node):
        if node not in self.parent or node == self.parent[node]:
            return node

        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return False

        if self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
        elif self.rank[parent2] < self.rank[parent1]:
            self.parent[parent2] = parent1
        else:
            self.parent[parent1] = parent2
            self.rank[parent1] += 1

        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        dsu = DSU()

        for edge in edges:
            if not dsu.union(edge[0], edge[1]):
                return edge

        return []
        