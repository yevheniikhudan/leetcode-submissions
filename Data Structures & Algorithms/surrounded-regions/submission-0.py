class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        dirs = ((-1, 0), (1, 0), (0, 1), (0, -1))
        q = deque()

        for row in range(rows):
            for col in range(cols):
                if (
                    row == 0 or col == 0 or row == rows - 1 or col == cols - 1
                ) and board[row][col] == "O":
                    q.append((row, col))

        while q:
            row, col = q.popleft()
            board[row][col] = "S"
            for dR, dC in dirs:
                newRow = row + dR
                newCol = col + dC
                if (
                    0 <= newRow < rows
                    and 0 <= newCol < cols
                    and board[newRow][newCol] == "O"
                ):
                    q.append((newRow, newCol))

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "S":
                    board[row][col] = "O"