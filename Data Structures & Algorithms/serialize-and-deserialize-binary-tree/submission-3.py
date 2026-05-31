# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Questions
    # 1. so it has to be one string after serializatoin?
    # 2. is there a certain way to process null node? does it have to be appeared as "null" in string?
    # 3. Can the tree be empty?

    # Approach
    # BFS level by level access

    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")

        return ",".join(result)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1

        while queue:
            node = queue.popleft()
            
            if nodes[i] == "null":
                node.left = None
            else:
                node.left = TreeNode(int(nodes[i]))
                queue.append(node.left)
            i += 1

            if nodes[i] == "null":
                node.right = None
            else:
                node.right = TreeNode(int(nodes[i]))
                queue.append(node.right)
            i += 1

        return root

    # Big O
    # Serialize O(N)
    # Deserialize O(N)
















