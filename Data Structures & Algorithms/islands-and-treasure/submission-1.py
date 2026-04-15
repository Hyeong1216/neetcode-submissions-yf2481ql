class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # BFS
        if not grid or not grid[0]:
            return
        
        rows, cols = len(grid), len(grid[0])
        LAND = 2147483647
        TREASURE = 0
        WATER = -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        q = deque()
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == TREASURE:
                    q.append((row, col))
        
        while q:
            curr_row, curr_col = q.popleft()
            for rDir, cDir in directions:
                nr, nc = curr_row + rDir, curr_col + cDir
                if nr >= 0 and nr < rows and \
                nc >= 0 and nc < cols and \
                grid[nr][nc] == LAND:
                    new_distance = grid[curr_row][curr_col] + 1
                    grid[nr][nc] = new_distance
                    q.append((nr,nc))
        #------------------------------------------------
        #bfs
        # if not grid or not grid[0]:
        #     return
            
        # rows, cols = len(grid), len(grid[0])
        # LAND = 2147483647
        # TREASURE = 0
        # WATER = -1

        # # Step 1: What should go in your initial queue?
        # # HInt: All starting points for BFS
        # q = collections.deque()
        # for i in range(rows):
        #     for j in range(cols):
        #         if grid[i][j] == TREASURE:
        #             q.append((i, j))
            
        # # Step 2: Multi-source BFS
        # while q:
        #     # Step 1: get current cell
        #     curr_row, curr_col = q.popleft()

        #     # Stpe 2: Explore all 4 neighbors
        #     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        #     for row_dir, col_dir in directions:
        #         new_row = curr_row + row_dir
        #         new_col = curr_col + col_dir
                
        #         if new_row >= 0 and new_row < rows and \
        #         new_col >= 0 and new_col < cols and \
        #         grid[new_row][new_col] == LAND:
        #             new_distance = grid[curr_row][curr_col] + 1
        #             grid[new_row][new_col] = new_distance
        #             q.append((new_row, new_col))


