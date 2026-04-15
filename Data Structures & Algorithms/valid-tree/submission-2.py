class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # dfs
        if len(edges) != n - 1:
            return False
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()

        def dfs(node, parent):
            if node in visited:
                return False
            
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor == parent:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True                    
        

        return dfs(0, -1) and len(visited) == n
        
        
        
        
        
        
        
        
        
        
        
        #-----------------------------------------------------------------
        # dfs
        # if len(edges) != n - 1:
        #     return False

        # graph = [[] for _ in range(n)]
        # for a, b in edges:
        #     graph[a].append(b)
        #     graph[b].append(a)

        # visited = set()

        # def dfs(node, parent):
        #     if node in visited:
        #         return False # Cycle detected
            
        #     visited.add(node)
            
        #     for neighbor in graph[node]:
        #         if neighbor == parent:
        #             continue # skip parents to avoid false cycle
        #         if not dfs(neighbor, node):
        #             return False # cycle found in subtree
        #     return True
        
        # # start DFS from node 0 with no parent (-1)
        # # Check for cycles AND ensure all nodes are visited(connected)
        # return dfs(0, -1) and len(visited) == n
            

        
        