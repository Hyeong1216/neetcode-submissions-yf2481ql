# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curr_max):
            if not node:
                return 0

            count = 1 if node.val >= curr_max else 0

            new_max = max(curr_max, node.val)
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)

            return count


        return dfs(root, root.val)