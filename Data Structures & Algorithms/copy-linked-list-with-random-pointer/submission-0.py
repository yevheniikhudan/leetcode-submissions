"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: Optional[Node], cache = {}) -> Optional[Node]:
        """
        Create a deep copy of a linked list with random pointers.

        Approach: Use a hash map to track old -> new node mappings
        1. First pass: Create all new nodes and map old -> new
        2. Second pass: Set next and random pointers using the map

        Time Complexity: O(n) - two passes through the list
        Space Complexity: O(n) - hash map to store node mappings
        """
        if head == None:
            return None
        
        if head in cache:
            return cache[head]
        
        copy = Node(head.val)
        cache[head] = copy
        copy.next = self.copyRandomList(head.next, cache)
        copy.random = cache[head.random] if head.random in cache else None
        
        return copy
        