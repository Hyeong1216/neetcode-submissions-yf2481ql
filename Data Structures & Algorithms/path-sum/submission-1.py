# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # Questions
        # 1. can there be negative numbers?
        # 2. is this balanced tree?
        # 3. What if tree is empty

        # Solution
        # DFS 써야함
        def dfs(node, remaining):
            if not node:
                return False
            remaining -= node.val
            if not node.left and not node.right and remaining == 0:
                return True
            
            return dfs(node.left, remaining) or dfs(node.right, remaining)
        
        return dfs(root, targetSum)
# Time: O(N) — 모든 노드 한 번씩 방문
# Space: O(H) — H는 tree 높이, call stack 깊이
#         balanced tree: O(log N)
#         worst case (skewed): O(N)