# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        # Define helper function for depth-first search
        # Takes current node and its depth (level) as parameters
        def dfs(node, depth):
            # Base case: if current node is None (null), stop recursion
            if not node:
                return None
            
            # Key insight: if depth equals length of result list,
            # this means we're visiting this level for the first time.
            # Since we explore right subtree first, this is the rightmost node at this level
            if depth == len(res):
                res.append(node.val)  # Add this node's value to result
            
            # Recursive calls: RIGHT FIRST, then left
            # This ensures we always see the rightmost node at each level first
            dfs(node.right, depth + 1)  # Explore right subtree at next depth level
            dfs(node.left, depth + 1)   # Explore left subtree at next depth level

        # Start DFS from root at depth 0
        dfs(root, 0)
        
        # Return the list of rightmost values from each level
        return res