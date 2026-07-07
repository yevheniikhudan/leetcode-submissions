class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
                elif grid[row][col] == 1:
                    fresh += 1

        while q and fresh > 0:
            for _ in range(len(q)):
                row, col = q.popleft()
                for dR, dC in directions:
                    newRow = row + dR
                    newCol = col + dC

                    if (
                        0 <= newRow < rows
                        and 0 <= newCol < cols
                        and grid[newRow][newCol] == 1
                    ):
                        q.append((newRow, newCol))
                        grid[newRow][newCol] = 2
                        fresh -= 1

            time += 1

        return time if fresh == 0 else -1
        return time