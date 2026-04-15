"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # DFS
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                cloned_nei = dfs(nei)
                oldToNew[node].neighbors.append(cloned_nei)
            return copy

        return dfs(node) if node else None
        #----------------------------------------------------------------------
        # bfs
        # if not node:
        #     return None
        
        # oldToNew = {}
        # # STEP 1: Create the initial clone
        # oldToNew[node] = Node(node.val)
        # q = collections.deque([node])

        # while q:
        #     cur = q.popleft()

        #     for nei in cur.neighbors:
        #         if nei not in oldToNew:
        #             oldToNew[nei] = Node(nei.val)
        #             q.append(nei)
        #         oldToNew[cur].neighbors.append(oldToNew[nei])
        # return oldToNew[node]

        #----------------------------------------------------------------------
        # dfs
        # oldToNew = {}

        # def dfs(node):
        #     # for cycle detection
        #     if node in oldToNew:
        #         return oldToNew.get(node)

        #     # put current node into the oldToNew
        #     copied_node = Node(node.val)
        #     oldToNew[node] = copied_node

        #     #do recursion
        #     for nei in node.neighbors:
        #         cloned_neighbor = dfs(nei)
        #         copied_node.neighbors.append(cloned_neighbor)
        #     return copied_node

        # return dfs(node) if node else None

        #----------------------------------------------------------------------
        #dfs
        # oldToNew = {} # HashMap to store mapping: original_node > cloned_node

        # def dfs(node):
        #     if node in oldToNew: #if we've already cloned this node
        #         return oldToNew[node] # return the existing clone (prevent infinite loops)
            
        #     copy = Node(node.val) # Create new node with same value as original
        #     oldToNew[node] = copy # store mapping BEFORE processing neighbors 

        #     for nei in node.neighbors: # iterate through all neighbors of current node
        #         copy.neighbors.append(dfs(nei)) # recursively clone each neighbor and add to copy's neighbor
            
        #     return copy
        # return dfs(node) if node else None
