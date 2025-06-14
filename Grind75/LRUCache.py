class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None


class LRUCache:
    # https://youtu.be/7ABFKPK2hD4
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # left = LRU, right = most recent
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def _remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev

    # insert node at right
    def _insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            #TODO: update most recent
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])

        if len(self.cache) > self.capacity:
            # remove from list and delete LRU from the hashmap
            lru = self.left.next
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
