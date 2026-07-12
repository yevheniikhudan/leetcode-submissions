class Node:
    def __init__(self, key = 0, next = None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.capacity = 10_007
        self.keys = [Node() for _ in range(self.capacity)]

    def add(self, key: int) -> None:
        cur = self.keys[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                return

            cur = cur.next

        cur.next = Node(key)

    def remove(self, key: int) -> None:
        cur = self.keys[self.hash(key)]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return

            cur = cur.next

    def contains(self, key: int) -> bool:
        cur = self.keys[self.hash(key)].next

        while cur:
            if cur.key == key:
                return True

            cur = cur.next

        return False

    def hash(self, key: int) -> int:
        return key % self.capacity
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)