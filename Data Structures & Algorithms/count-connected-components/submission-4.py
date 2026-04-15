class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # DFS
        # 1. construct undirected graph
        # 2. initialize count and tracking set
        # 3. dfs method
        # 4. run dfs
        # 5. return count variable
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        count = 0
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count



        #----------------------------
        #DFS answer
        # graph = [[] for _ in range(n)]

        # for a, b in edges:
        #     graph[a].append(b)
        #     graph[b].append(a)

        # count = 0
        # visited = set()

        # def dfs(node):
        #     visited.add(node)
        #     for neighbor in graph[node]:
        #         if neighbor not in visited:
        #             dfs(neighbor)
        
        # for node in range(n):
        #     if node not in visited:
        #         dfs(node)
        #         count += 1
        
        # return count