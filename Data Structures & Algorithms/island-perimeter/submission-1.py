class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 1
            if (row, col) in visited:
                return 0
            
            visited.add((row, col))
            
            return dfs(row, col + 1) + dfs(row + 1, col) + dfs(row, col - 1) + dfs(row - 1, col)
        


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return dfs(row, col)
        return 0