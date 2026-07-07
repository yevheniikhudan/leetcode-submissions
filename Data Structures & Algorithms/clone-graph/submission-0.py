"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        seen = {}

        def dfs(node):
            if not node:
                return

            if node in seen:
                return seen[node]

            clone = Node(node.val)
            seen[node] = clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone


        return dfs(node)
        