class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose() -> None:
            for row in range(len(matrix)):
                for col in range(row + 1, len(matrix[row])):
                    matrix[row][col], matrix[col][row] = (
                        matrix[col][row],
                        matrix[row][col],
                    )

        def reverse() -> None:
            for row in matrix:
                row.reverse()

        transpose()
        reverse()
        