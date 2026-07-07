# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        if root:
            q.append(root)

        while q:
            qSize = len(q)

            for i in range(qSize):
                cur = q.popleft()

                if cur.left:
                    q.append(cur.left)

                if cur.right:
                    q.append(cur.right)

                if i == qSize - 1:
                    res.append(cur.val)
        return res