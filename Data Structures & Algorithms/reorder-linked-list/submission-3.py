# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse(head):
            prev, curr = None, head
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            return prev
        
        #Step 1: Find the middle of the list using slow and fast pointers
        if not head or not head.next:
            return
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #Step 2: Reverse the second half of the list starting from slow
        second_half = reverse(slow.next)
        slow.next = None

        #Step 3: Merge the two halves
        first_half = head
        while second_half:
            temp1, temp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = temp1
            first_half = temp1
            second_half = temp2
