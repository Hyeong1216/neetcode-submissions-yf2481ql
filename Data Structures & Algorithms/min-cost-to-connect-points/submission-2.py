class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's algorithm
        n = len(points)

        visited = set()
        visited.add(0)
        heap = []

        def manhattan(i, j):
            return abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1])



        for i in range(1, n):
            heapq.heappush(heap, (manhattan(0, i), i))
        
        total_cost = 0

        while len(visited) < n:
            cost, i = heapq.heappop(heap)

            if i in visited:
                continue
            visited.add(i)
            total_cost += cost

            for j in range(0, n):
                if j not in visited:
                    heapq.heappush(heap, (manhattan(i, j), j))
            

        


        return total_cost






















        #--------------------------------------------------
        # Prim's algorithm
        # n = len(points)

        # # Helper function to calculate Manhattan distance
        # def manhattan_distance(i, j):
        #     return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])  
        
        # visited = set()

        # heap = []

        # visited.add(0)

        # for i in range(1, n):
        #     cost = manhattan_distance(0, i)
        #     heapq.heappush(heap, (cost, i))

        # total_cost = 0
        # while len(visited) < n:
        #     print(f"heap:{heap}")

        #     # TODO: Get minimum cost edge from heap
        #     cost, node = heapq.heappop(heap)
            
        #     # TODO: Skip if node already visited
        #     if node in visited:
        #         continue

        #     # TODO: Add node to MST and update total_cost
        #     visited.add(node)
        #     total_cost += cost

        #     # TODO: Add edges from this new node to all unvisited nodes
        #     for i in range(0, n):  # Check ALL nodes
        #         if i not in visited:  # But only add edges to unvisited ones
        #             heapq.heappush(heap, (manhattan_distance(node, i), i))


        # return total_cost
