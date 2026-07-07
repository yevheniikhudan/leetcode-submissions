class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = [[] for _ in range(numCourses)]
        inEdges = [0] * numCourses
        q = deque()
        coursesFinished = 0

        for dest, src in prerequisites:
            inEdges[dest] += 1
            adjList[src].append(dest)

        for i in range(numCourses):
            if inEdges[i] == 0:
                q.append(i)

        while q:
            coursesFinished += 1
            course = q.popleft()

            for adj in adjList[course]:
                if inEdges[adj] > 0:
                    inEdges[adj] -= 1

                if inEdges[adj] == 0:
                    q.append(adj)


        return coursesFinished == numCourses
        