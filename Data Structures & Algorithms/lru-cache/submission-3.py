class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # Questions:
    # 1. can test cases possibly increase the size of LRU cache?
    # 2. what should get return if key does not exist
    # 3. Is capacity always at least 1?

    # Approach
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key -> Node
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:  
        # 1. key가 cache에 없으면 → -1 반환
        # 2. 있으면 → 해당 노드를 MRU 위치로 이동 (remove 후 insert)
        # 3. value 반환
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        # 1. key가 이미 cache에 있으면 → 제거
        # 2. 새 노드 생성해서 cache에 추가하고 insert
        # 3. capacity 초과하면 → LRU 제거 (head.next가 LRU)
        if key in self.cache:
            self.remove(self.cache[key])
        
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
        
