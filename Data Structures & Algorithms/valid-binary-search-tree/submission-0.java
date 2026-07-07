/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public boolean isValidBST(TreeNode root) {
        if (root == null) {
            return true;
        }

        return dfs(root.left, root.val, Integer.MIN_VALUE) &&
        dfs(root.right, Integer.MAX_VALUE, root.val);
    }

    private boolean dfs(TreeNode root, int maxVal, int minVal) {
        if (root == null) {
            return true;
        }

        int newMax = Math.min(maxVal, root.val);
        int newMin = Math.max(minVal, root.val);

        return root.val > minVal &&
                root.val < maxVal &&
                dfs(root.left, root.val, minVal) &&
                dfs(root.right, maxVal, root.val);
    }
}
