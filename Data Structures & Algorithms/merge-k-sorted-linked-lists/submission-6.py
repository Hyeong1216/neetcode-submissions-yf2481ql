class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for l in lists:
            curr = l
            while curr:
                num = curr.val
                heapq.heappush(heap, num)
                curr = curr.next
        
        dummy = ListNode()
        head = ListNode()
        dummy.next = head
        while heap:
            curr_val = heapq.heappop(heap)

            # print(curr_val)
            head.next = ListNode(curr_val)
            head = head.next
        


        return dummy.next.next
            








































# class Solution:    
#     def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
#         # Questions:
#         # 1. Are all linked lists the same size?
#         # 2. Can the input be empty?
#         # 3. Can any individual list be empty?

#         # Approach: Min-heap — O(N log K)
#         # Key insight: heap size stays at k throughout
#         # Each pop → add that node's next → heap stays balanced
#         # i as tie-breaker (ListNode is not comparable)

#         heap = []
#         for i, node in enumerate(lists):
#             if node:
#                 heapq.heappush(heap, (node.val, i, node))
        
#         dummy = ListNode(0)
#         curr = dummy

#         while heap:
#             val, i, node = heapq.heappop(heap)
#             curr.next = node
#             curr = curr.next
#             if node.next:
#                 heapq.heappush(heap, (node.next.val, i, node.next))

#         return dummy.next

#         # Time: O(N log K) — N nodes, heap size K maintained throughout
#         # Space: O(K) — heap stores at most one node per list