class DSU:
    def __init__(self, n):
        self.Parent = list(range(n+1))
        self.Size = [1] * (n+1)

    def find(self, x):
        if self.Parent[x] == x:
            return x
        return self.find(self.Parent[x])

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.Parent[root_x] = root_y
        
    
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Kruskal's algorithm
        n = len(points)

        # Step 1: Create all possible edges with their costs
        edges = []
        for i in range(n):
            for j in range(i+1, n):
                cost = abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])
                edges.append((cost, i, j))
        
        # Step 2: Sort edges by cost
        edges.sort()

        # Step 3: Initialize Union-Find
        uf = DSU(n)

        # Step 4: Process edges in order
        total_cost = 0
        edges_used = 0
        

        for cost, u, v in edges:
            # TODO: Check if u and v would create a cycle
            # If not, add this edge to MST
            if not uf.connected(u, v):
                uf.union(u, v)
                total_cost += cost
                edges_used += 1
            
                # TODO: Stop when we have n-1 edges (complete MST)
                if edges_used == n-1:
                    break
            
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
