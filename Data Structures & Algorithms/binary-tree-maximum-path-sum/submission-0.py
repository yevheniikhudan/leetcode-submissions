# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxSum = float("-inf")

        def dfs(root):
            nonlocal maxSum

            if not root:
                return 0

            currentSum = root.val
            leftSum = max(dfs(root.left), 0)
            rightSum = max(dfs(root.right), 0)

            currentSum += max(leftSum, rightSum)

            maxSum = max(maxSum, root.val + leftSum + rightSum)

            return currentSum

        dfs(root)
        return maxSum