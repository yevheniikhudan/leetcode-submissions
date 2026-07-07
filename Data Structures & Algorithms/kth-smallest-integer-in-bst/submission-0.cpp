/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
    vector<int> inorder;
    int k;

   public:
    /**
     * Find the kth smallest element in a BST.
     *
     * @param root Root of the binary search tree
     * @param k The k value (1-indexed)
     * @return The kth smallest value in the BST
     */
    int kthSmallest(TreeNode* root, int k) {
        this->k = k;
        inorder.clear();  // Clear the vector for each test case
        dfs(root);

        return inorder[k - 1];
    }

   private:
    void dfs(TreeNode* root) {
        if (!root) {
            return;
        }
        if (inorder.size() == k) {
            return;
        }

        dfs(root->left);
        inorder.push_back(root->val);
        dfs(root->right);
    }
};
