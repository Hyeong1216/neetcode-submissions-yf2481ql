class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # BFS
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visited.add((row, col))

            while q:
                curr_row, curr_col = q.popleft()
                for rowDir, colDir in directions:
                    nr, nc = curr_row + rowDir, curr_col + colDir
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited or grid[nr][nc] == "0":
                        continue
                    q.append((nr, nc))
                    visited.add((nr, nc))

        
        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    count += 1
                

        return count