class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def dfs(row, col):
            if row < 0 or row >= rows or \
            col < 0 or col >= cols or \
            (row, col) in visited or \
            grid[row][col] == 0:
                return 0
            visited.add((row, col))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            area = 1
            for rowDir, colDir in directions:
                area += dfs((row+rowDir), (col+colDir))
            return area

        for row in range(rows):
            for col in range(cols):
                if (row, col) not in visited and grid[row][col] == 1:
                    curr_area = dfs(row, col)
                    maxArea = max(maxArea, curr_area)

        return maxArea
        #------------------------------------------------
        # if not grid:
        #     return 0
        
        # rows, cols = len(grid), len(grid[0])
        # islands = 0
        # visited = set()
        # def dfs(row, col):
        #     if row < 0 or row >= rows or \
        #     col < 0 or col >= cols or \
        #     (row, col) in visited or \
        #     grid[row][col] == 0:
        #         return
        #     visited.add((row, col))
        #     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        #     for rowDir, colDir in directions:
        #         dfs((row+rowDir), (col+colDir))


        # for row in range(rows):
        #     for col in range(cols):
        #         if (row, col) not in visited and grid[row][col] == 1:
        #             dfs(row, col)
        #             islands += 1
        # return islands