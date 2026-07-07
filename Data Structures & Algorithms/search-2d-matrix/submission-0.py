class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])
        left, right = 0, height * width - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_col = mid % width
            mid_row = mid // width

            if target > matrix[mid_row][mid_col]:
                left = mid + 1
            elif target < matrix[mid_row][mid_col]:
                right = mid - 1
            else:
                return True

        return False