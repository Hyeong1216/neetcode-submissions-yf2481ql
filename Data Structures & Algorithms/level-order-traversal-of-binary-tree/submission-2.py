# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        result = []
        q = collections.deque()
        q.append(root)
        while q:
            level = []
            
            for i in range(len(q)):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            result.append(level)
        return result
        
        
        
        
        
        
        #-----------------
        # if not root:
        #     return []
        # result = []
        # queue = deque([root])

        # while queue:
        #     level = []
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         level.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     result.append(level)
        # return result
        