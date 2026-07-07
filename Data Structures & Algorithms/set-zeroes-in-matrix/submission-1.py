class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        firstRowZeroed = False
        firstColumnZeroed = False

        for col in range(cols):
            if matrix[0][col] == 0:
                firstRowZeroed = True
                break

        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                firstColumnZeroed = True
                break

        for row in range(1, rows):
            for col in range(1, cols):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        for col in range(1, cols):
            if matrix[0][col] == 0:
                for row in range(1, rows):
                    matrix[row][col] = 0

        for row in range(rows):
            if matrix[row][0] == 0:
                for col in range(1, cols):
                    matrix[row][col] = 0

        if firstRowZeroed:
            for col in range(cols):
                matrix[0][col] = 0

        if firstColumnZeroed:
            for row in range(rows):
                matrix[row][0] = 0