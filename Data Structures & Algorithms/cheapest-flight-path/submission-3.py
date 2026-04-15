class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # BFS
        graph = {}
        for from_airport, to_airport, price in flights:
            if from_airport not in graph:
                graph[from_airport] = []
            graph[from_airport].append((to_airport, price))
        min_cost = float('inf')
        q = deque()
        q.append((src, 0, 0))

        while q:
            curr_airport, curr_cost, stops_used = q.popleft()

            if curr_airport == dst:
                min_cost = min(min_cost, curr_cost)
            
            if stops_used > k:
                continue
            
            if curr_cost >= min_cost:
                continue
            
            if curr_airport in graph:
                for next_airport, price in graph[curr_airport]:
                    q.append((next_airport, curr_cost + price, stops_used + 1))
        return min_cost if min_cost != float('inf') else -1
        #-----------------------------------------------------------------
        # DFS
        # graph = {}
        
        # # graph[airport] = [(destination, price), (destination, price), ...]
        # for from_airport, to_airport, price in flights:
        #     if from_airport not in graph:
        #         graph[from_airport] = []
        #     graph[from_airport].append((to_airport, price))


        # # Track the minimum cost found so far (for pruning)
        # min_cost = [float('inf')]

        # def dfs(curr_airport, curr_cost, stops_used):
        #     # Base case 1: reached destination
        #     if curr_airport == dst:
        #         min_cost[0] = min(min_cost[0], curr_cost)

        #     # Base case 2: used too many stops
        #     if stops_used > k:
        #         return

        #     # Pruning: if current cost already exceeds best known cost
        #     if curr_cost >= min_cost[0]:
        #         return
            
        #     # Explore all flights from current airport
        #     if curr_airport in graph:
        #         for next_airport, flight_price in graph[curr_airport]:
        #             dfs(next_airport, curr_cost + flight_price, stops_used + 1)
                    
        # dfs(src, 0, 0)

        # return min_cost[0] if min_cost[0] != float('inf') else -1