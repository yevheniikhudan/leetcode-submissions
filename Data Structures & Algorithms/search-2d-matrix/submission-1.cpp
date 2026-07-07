class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int cols = matrix[0].size();
        int rows = matrix.size();
        int left = 0, right = cols * rows - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            int mid_col = mid % cols;
            int mid_row = mid / cols;
            if (target > matrix[mid_row][mid_col]) {
                left = mid + 1;
            } else if (target < matrix[mid_row][mid_col]) {
                right = mid - 1;
            } else {
                return true;
            }
        }
        return false;
    }
};
