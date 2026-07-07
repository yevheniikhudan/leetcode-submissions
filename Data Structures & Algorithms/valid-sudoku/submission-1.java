class Solution {
    public boolean isValidSudoku(char[][] board) {
        int[] rows = new int[9];
        int[] cols = new int[9];
        int[] boxes = new int[9];

        for (int row = 0; row < 9; row++) {
            for (int col = 0; col < 9; col++) {
                char cell = board[row][col];
                if (cell == '.') {
                    continue;
                }

                int val = 1 << ((cell - '0') - 1);
                if ((rows[row] & val) != 0) {
                    return false;
                }
                if ((cols[col] & val) != 0) {
                    return false;
                }
                if ((boxes[row / 3 * 3 + col / 3] & val) != 0) {
                    return false;
                }

                rows[row] |= val;
                cols[col] |= val;
                boxes[row / 3 * 3 + col / 3] |= val;
            }
        }
        return true;
    }
}
