class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # BFS
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()
        count = 0
        for node in range(n):
            if node not in visited:
                q = collections.deque([node])
                visited.add(node)

                while q:
                    curr_node = q.popleft()
                    for neighbor in graph[curr_node]:
                        if neighbor not in visited:
                            q.append(neighbor)
                            visited.add(neighbor)
                count += 1
                
        return count
        #------------------------------------------
        # DFS
        # 1. construct undirected graph
        # 2. initialize count and tracking set
        # 3. dfs method
        # 4. run dfs
        # 5. return count variable

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