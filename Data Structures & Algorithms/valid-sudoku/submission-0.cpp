class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        vector<int> rows(9, 0);
        vector<int> cols(9, 0);
        vector<int> boxes(9, 0);

        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                char cell = board[row][col];
                if (cell == '.') {
                    continue;
                }

                int val = 1 << ((cell - '0') - 1);
                if (rows[row] & val || cols[col] & val || boxes[row / 3 * 3 + col / 3] & val){
                    return false;
                }

                rows[row] |= val;
                cols[col] |= val;
                boxes[row / 3 * 3 + col / 3] |= val;
            }
        }

        return true;
    }
};
