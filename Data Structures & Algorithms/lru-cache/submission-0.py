class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
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
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.add_to_end(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value

            self.remove(node)
            self.add_to_end(node)

        else:
            node = Node(key, value)
            self.cache[key] = node
            self.add_to_end(node)

            if len(self.cache) > self.capacity:
                oldest = self.head.next
                self.remove(oldest)
                del self.cache[oldest.key]

    # 自己添加的辅助方法
    def remove(self, node):
        before = node.prev
        after = node.next

        before.next = after
        after.prev = before

    # 自己添加的辅助方法
    def add_to_end(self, node):
        before = self.tail.prev

        before.next = node
        node.prev = before

        node.next = self.tail
        self.tail.prev = node