class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        """
        Initialize the LRU cache with positive size capacity.

        Args:
            capacity: Maximum number of items the cache can hold
        """
        self.capacity = capacity
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.cache = {}
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        """
        Return the value of the key if the key exists, otherwise return -1.

        Args:
            key: The key to look up

        Returns:
            The value associated with the key, or -1 if not found

        Time Complexity: O(1)
        """
        if key not in self.cache:
            return -1
        
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
        
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        """
        Update the value of the key if the key exists. Otherwise, add the key-value
        pair to the cache. If the number of keys exceeds the capacity from this
        operation, evict the least recently used key.

        Args:
            key: The key to add or update
            value: The value to associate with the key

        Time Complexity: O(1)
        """
        if key in self.cache:
            self.remove(self.cache[key])
            
        node = Node(key, value)
        self.add(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
        
    def add(self, node: Node) -> None:
        prev = self.right.prev
        nxt =  self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
        
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
