class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjList = [[] for _ in range(numCourses)]
        inEdges = [0] * numCourses
        q = deque()
        path = []

        for dest, src in prerequisites:
            inEdges[dest] += 1
            adjList[src].append(dest)

        for i in range(numCourses):
            if inEdges[i] == 0:
                q.append(i)

        while q:
            course = q.popleft()
            path.append(course)

            for adj in adjList[course]:
                if inEdges[adj] > 0:
                    inEdges[adj] -= 1

                if inEdges[adj] == 0:
                    q.append(adj)

        return path if len(path) == numCourses else []