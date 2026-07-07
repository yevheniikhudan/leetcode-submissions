# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {val: index for index, val in enumerate(inorder)}
        preId = 0

        def dfs(left, right):
            nonlocal preId
            if left > right:
                return None

            root = TreeNode(preorder[preId])
            mid = indices[root.val]
            preId += 1

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)