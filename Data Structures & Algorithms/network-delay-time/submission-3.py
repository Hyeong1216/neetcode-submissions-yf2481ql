class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Dijkstra

        # Step 1: build adjacency list
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        # Step 2: Initialize distances and priority queue
        distances = {} #node -> shortest distance from k
        pq = [(0, k)] # (distance, node) - start from k with distance 0

        # Step 3: Dijkstra's main loop
        while pq:
            curr_dist, node = heapq.heappop(pq)

            if node in distances:
                continue
            
            distances[node] = curr_dist

            for v, t in graph[node]:
                if v not in distances:
                    heapq.heappush(pq, (curr_dist+t, v))
                    # pq.append((curr_dist+t, v))

            

        if len(distances) != n:
            return -1
        return max(distances.values())
        
        #-----------------------------------------------------------------

        # Step 1: Build adjacency list
        # Step 2: Track minimum time to reach each node
        # Step 3: Start DFS from k
        # Step 4: check if all nodes reachable and return max time
        # graph = defaultdict(list)
        # for u, v, t in times:
        #     graph[u].append((v, t))
        # min_time = {}
        # def dfs(node, curr_time, visited):
        #     if node in min_time and curr_time >= min_time[node]:
        #         return
        #     min_time[node] = curr_time

        #     if node in visited:
        #         return
        #     visited.add(node)
        #     for v, t in graph[node]:
        #         dfs(v, curr_time + t, visited)
        #     visited.remove(node)


        # dfs(k, 0, set())
        # if len(min_time) != n:
        #     return -1
        # return max(min_time.values())












        #-----------------------------------------------------------------
        # DFS 
        # Step 1: Build adjacency list
        # graph = defaultdict(list)
        # for u, v, t in times:
        #     graph[u].append((v, t)) # (neighbor, weight)
        
        # # Step 2: Track minimum time to reach each node
        # min_time = {} #node -> minimum time to reach it

        # def dfs(node, current_time, visited):
        #     if node in min_time and current_time >= min_time[node]:
        #         return
            
        #     # update the shortest time to reach this node
        #     min_time[node] = current_time
            
        #     # Avoid infinite cycles in the current path
        #     if node in visited:
        #         return
        #     visited.add(node)

        #     for neighbor, weight in graph[node]:
        #         dfs(neighbor, current_time + weight, visited)

        #     visited.remove(node)
        
        # # Step 3: Start DFS from k
        # dfs(k, 0, set())

        # # Step 4: check if all nodes reachable and return max time
        
        # if len(min_time) != n: # if some nodes are unreachable
        #     return -1
        # return max(min_time.values())

         


