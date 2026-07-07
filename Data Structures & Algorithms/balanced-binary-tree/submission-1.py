# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal balanced

            if not root:
                return 0

            max_left = dfs(root.left)
            max_right = dfs(root.right)

            balanced = balanced and abs(max_left - max_right) <= 1

            return max(dfs(root.left), dfs(root.right)) + 1

        dfs(root)

        return balanced