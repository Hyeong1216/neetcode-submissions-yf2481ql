class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # BFS
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(r, c):
            q = deque([(r, c)])
            visited.add((r, c))
            perim = 0
            
            while q:
                x, y = q.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny < 0 or nx >= rows or ny >= cols or grid[nx][ny] == 0:
                        perim += 1
                    elif (nx, ny) not in visited:
                        visited.add((nx, ny))
                        q.append((nx, ny))
            return perim
        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return bfs(row, col)
        return 0

        # DFS
        # rows, cols = len(grid), len(grid[0])
        # visited = set()

        # def dfs(row, col):
        #     if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
        #         return 1
        #     if (row, col) in visited:
        #         return 0
            
        #     visited.add((row, col))
            
        #     return dfs(row, col + 1) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row - 1, col)
        


        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == 1:
        #             return dfs(row, col)
        # return 0