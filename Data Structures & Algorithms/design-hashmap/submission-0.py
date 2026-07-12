class Node:
    def __init__(self, key = 0, val = 0, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.capacity = 1009
        self.hashMap = [Node() for _ in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        node = self.hashMap[key % self.capacity] # dummy node

        while node.next: # iterate through linked list
            if node.next.key == key:
                node.next.val = value
                return
            node = node.next # go to the next node

        node.next = Node(key, value)

    def get(self, key: int) -> int:
        node = self.hashMap[key % self.capacity].next

        while node:
            if node.key == key:
                return node.val
            node = node.next

        return -1

    def remove(self, key: int) -> None:
        node = self.hashMap[key % self.capacity]

        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)