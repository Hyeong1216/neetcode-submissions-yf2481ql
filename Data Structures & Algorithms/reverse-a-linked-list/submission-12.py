# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev, curr = None, head
        # while curr:
        #     curr.next, prev, curr = prev, curr, curr.next
        # return prev
        

        prev, curr = None, head
        while curr:
            temp = curr.next # save relation to the next node before changing direction
            curr.next = prev # change direction
            prev = curr # advance prev to curr
            curr = temp # advance curr to original curr.next
        return prev


