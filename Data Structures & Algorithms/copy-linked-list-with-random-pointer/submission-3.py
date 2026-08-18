"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # hashmap
        # 1. Map old node with new node
        if not head:
            return None
        oldToNew = {}
        curr = head
        while curr:
            oldToNew[curr] = Node(curr.val)
            curr = curr.next

        # 2. Copy relations
        curr = head
        while curr:
            if curr.next:
                oldToNew[curr].next = oldToNew[curr.next]
            if curr.random:
                oldToNew[curr].random = oldToNew[curr.random]
            curr = curr.next
        return oldToNew[head]
        