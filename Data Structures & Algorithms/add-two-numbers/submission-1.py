# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev, curr = None, node
            while curr:
                curr.next, prev, curr = prev, curr, curr.next
            return prev
        
        l1_r = reverse(l1)
        l2_r = reverse(l2)

        num1, num2 = "", ""
        curr = l1_r
        while curr:
            num1 += str(curr.val)
            curr = curr.next
        # print(num1)

        curr = l2_r
        while curr:
            num2 += str(curr.val)
            curr = curr.next
        # print(num2)

        num3 = int(num1) + int(num2)
        # print(num3)

        num3 = str(num3)
        
        dummy = ListNode()
        curr = dummy
        for i in range(len(num3)):
            curr_num = num3[i]
            curr.next = ListNode(int(curr_num))
            curr = curr.next
        return reverse(dummy.next)
        
