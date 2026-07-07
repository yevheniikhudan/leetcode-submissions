class UnionFind:
    
    def __init__(self, n: int):
        self.parent = [n for n in range(n)]
        self.rank = [0] * n
        self.components = n

    def find(self, x: int) -> int:
        if self.parent[x] == x:
            return x

        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        p1 = self.find(x)
        p2 = self.find(y)

        return p1 == p2

    def union(self, x: int, y: int) -> bool:
        p1 = self.find(x)
        p2 = self.find(y)

        if p1 == p2:
            return False

        if self.rank[p1] < self.rank[p2]:
            self.parent[p1] = p2
        elif self.rank[p2] < self.rank[p1]:
            self.parent[p2] = p1
        else:
            self.parent[p1] = p2
            self.rank[p2] += 1

        self.components -= 1

        return True

    def getNumComponents(self) -> int:
        return self.components
