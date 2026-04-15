# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        current = head

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        while current:
            if self.hasKNodes(current, k):
                group_head = current
                prev, curr = None, current
                for _ in range(k):
                    temp = curr.next
                    curr.next = prev
                    prev = curr
                    curr = temp
                
                group_prev.next = prev
                group_head.next = curr
                group_prev = group_head
                current = curr
            else:
                break

        return dummy.next



    def hasKNodes(self, head, k):
        current = head
        count = 0
        while current and count < k:
            current = current.next
            count += 1
        return count == k