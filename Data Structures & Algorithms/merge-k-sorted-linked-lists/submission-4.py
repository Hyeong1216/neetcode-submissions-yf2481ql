# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Questions:
        # 1. is all linked lists the same size?
        # 2. is it possible that we get the empty input?

        # Answer
        # Heap
        heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))
        print(heap)
        dummy = ListNode(0)
        curr = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummy.next


        #-----------------------------------------------

        # Questions:
        # 1. is all linked lists the same size?
        # 2. is it possible that we get the empty input?

        # Heap
        # heap = []
        # for i, node in enumerate(lists):
        #     if node:
        #         heapq.heappush(heap, (node.val, i, node))
        
        # dummy = ListNode(0)
        # curr = dummy
        # while heap:
        #     val, i, node = heapq.heappop(heap)
        #     curr.next = node
        #     curr = curr.next
        #     if node.next:
        #         heapq.heappush(heap, (node.next.val, i, node.next))
        # return dummy.next

# # Time: O(n log k) — n nodes, heap size k maintained throughout
