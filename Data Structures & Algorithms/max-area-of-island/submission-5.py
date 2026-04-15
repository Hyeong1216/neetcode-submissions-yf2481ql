class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS
        if not grid:
            return 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(row, col):
            if row < 0 or row >= rows or \
            col < 0 or col >= cols or \
            grid[row][col] == 0 or \
            (row, col) in visited:
                return 0
            
            visited.add((row, col))
            area = 1
            for rowDir, colDir in directions:
                nr, nc = row + rowDir, col + colDir
                area += dfs(nr, nc)

            return area
        

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(max_area, dfs(row, col))

        return max_area

        #------------------------------------
        # BFS solution
        # if not grid:
        #     return 0
        # rows, cols = len(grid), len(grid[0])
        # maxArea = 0
        # visited = set()
        
        # def bfs(row, col):
        #     q = collections.deque()
        #     q.append((row, col))
        #     visited.add((row, col))
        #     curr_area = 0

        #     while q:
        #         curr_area += 1
        #         curr_row, curr_col = q.popleft()
        #         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        #         for rowDir, colDir in directions:
        #             newRow = curr_row + rowDir
        #             newCol = curr_col + colDir
        #             if newRow >= 0 and newCol >= 0 and \
        #             newRow < rows and newCol < cols and \
        #             grid[newRow][newCol] == 1 and \
        #             (newRow, newCol) not in visited:
        #                 q.append((newRow, newCol))
        #                 visited.add((newRow, newCol))
        #     return curr_area

        # for row in range(rows):
        #     for col in range(cols):
        #         if (row, col) not in visited and grid[row][col] == 1:
        #             curr_area = bfs(row, col)
        #             maxArea = max(maxArea, curr_area)

        # return maxArea
        #------------------------------------------------
        # DFS solution
        # if not grid:
        #     return 0
        
        # rows, cols = len(grid), len(grid[0])
        # visited = set()
        # maxArea = 0

        # def dfs(row, col):
        #     if row < 0 or row >= rows or \
        #     col < 0 or col >= cols or \
        #     (row, col) in visited or \
        #     grid[row][col] == 0:
        #         return 0
        #     visited.add((row, col))
        #     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        #     area = 1
        #     for rowDir, colDir in directions:
        #         area += dfs((row+rowDir), (col+colDir))
        #     return area

        # for row in range(rows):
        #     for col in range(cols):
        #         if (row, col) not in visited and grid[row][col] == 1:
        #             curr_area = dfs(row, col)
        #             maxArea = max(maxArea, curr_area)

        # return maxArea
