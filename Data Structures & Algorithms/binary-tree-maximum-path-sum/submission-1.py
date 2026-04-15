# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float('-inf')

        def helper(node):
            if not node:
                return 0
            
            left = max(0, helper(node.left))   # best path going down from left (ignore if negative)
            right = max(0, helper(node.right)) # best path going down from right (ignore if negative)
            
            # Path through current node (bridges left and right)
            current_max = node.val + left + right
            self.max_sum = max(self.max_sum, current_max)

            return node.val + max(left, right)
        
        helper(root)
        return self.max_sum