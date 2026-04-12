class Node:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
            self._insert_front(node)
            return node.val
        
        return -1

    def _remove(self, node: Node):
        p, n = node.prev, node.next
        p.next, n.prev = n, p

    def _insert_front(self, node: Node):
        first = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = first
        first.prev = node

    def put(self, key: int, value: int) -> None:
    
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove(node)
            self._insert_front(node)
        
        else:
            node = Node(key, value)
            self.cache[key] = node
            self._insert_front(node)

            if (len(self.cache)) > self.capacity:
                node = self.tail.prev
                self._remove(node)
                del self.cache[node.key]