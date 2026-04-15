class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or
                r == ROWS or
                c < 0 or
                c == COLS or
                grid[r][c] == 0 or
                (r, c) in visit):
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c)
                      + dfs(r - 1, c)
                      + dfs(r, c + 1)
                      + dfs(r, c - 1))
        area = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visit:
                    area = max(area, dfs(row, col))

        return area
                    
