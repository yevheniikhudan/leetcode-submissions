class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        h = [[grid[0][0], 0, 0]]
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visit.add((0, 0))

        while h:
            time, row, col = heapq.heappop(h)
            if row == n - 1 and col == n - 1:
                return time

            for dR, dC in directions:
                newRow, newCol = row + dR, col + dC
                if 0 <= newRow < n and 0 <= newCol < n and (newRow, newCol) not in visit:
                    visit.add((newRow, newCol))
                    heapq.heappush(h, [max(time, grid[newRow][newCol]), newRow, newCol])