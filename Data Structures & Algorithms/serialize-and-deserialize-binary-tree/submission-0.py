# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(root):
            if not root:
                res.append('N')
                return

            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        
        nodes = data.split(',')
        idX = 0
        def dfs():
            nonlocal idX

            if nodes[idX] == 'N':
                idX += 1
                return None

            root = TreeNode(int(nodes[idX]))
            idX += 1
            root.left = dfs()
            root.right = dfs()

            return root

        return dfs()
