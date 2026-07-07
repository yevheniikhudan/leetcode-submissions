class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [[-1, 0], [0, -1], [1, 0], [0, 1]]

        def dfs(row: int, col: int, pathLength: int) -> bool:
            if pathLength >= len(word):
                return True

            if row < 0:
                return False
            if col < 0:
                return False
            if row == ROWS:
                return False
            if col == COLS:
                return False
            if board[row][col] == "#":
                return False
            if board[row][col] != word[pathLength]:
                return False

            board[row][col] = "#"

            res = any(dfs(row + rD, col + cD, pathLength + 1) for rD, cD in directions)
            board[row][col] = word[pathLength]

            return res

        for row in range(ROWS):
            for col in range(COLS):
                if dfs(row, col, 0):
                    return True

        return False 