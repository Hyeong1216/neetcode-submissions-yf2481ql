class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        # Helper function to calculate Manhattan distance
        def manhattan_distance(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])  
        
        visited = set()

        heap = []

        visited.add(0)

        for i in range(1, n):
            cost = manhattan_distance(0, i)
            heapq.heappush(heap, (cost, i))
        total_cost = 0
        print(f"heap:{heap}")
        while len(visited) < n:
            # TODO: Get minimum cost edge from heap
            cost, node = heapq.heappop(heap)
            
            # TODO: Skip if node already visited
            if node in visited:
                continue

            # TODO: Add node to MST and update total_cost
            visited.add(node)
            total_cost += cost

            # TODO: Add edges from this new node to all unvisited nodes
            for i in range(0, n):  # Check ALL nodes
                if i not in visited:  # But only add edges to unvisited ones
                    heapq.heappush(heap, (manhattan_distance(node, i), i))


        return total_cost
