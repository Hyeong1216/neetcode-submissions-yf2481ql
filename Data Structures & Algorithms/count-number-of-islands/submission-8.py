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
                    if nr < 0 or nr >= rows or \
                    nc < 0 or nc >= cols or \
                    (nr, nc) in visited or \
                    grid[nr][nc] == "0":
                        continue
                    q.append((nr, nc))
                    visited.add((nr,nc))

        count = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    count += 1

        return count

        #----------------------------------------------
        # # DFS
        # if not grid:
        #     return 0
        # rows, cols = len(grid), len(grid[0])
        # visited = set()
        # count = 0
        # def dfs(row, col):
        #     if row < 0 or row >= rows or \
        #     col < 0 or col >= cols or \
        #     (row, col) in visited or \
        #     grid[row][col] == "0":
        #         return
        #     visited.add((row, col))
        #     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        #     for rowDir, colDir in directions:
        #         newRow = row + rowDir
        #         newCol = col + colDir
        #         dfs(newRow, newCol)
        
        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == "1" and (row, col) not in visited:
        #             dfs(row, col)
        #             count += 1

        # return count












        # # DFS
        # if not grid:
        #     return 0

        # rows, cols = len(grid), len(grid[0])
        # islands = 0
        # visited = set()
        # def dfs(row, col):
        #     if row < 0 or row >= rows or \
        #     col < 0 or col >= cols or \
        #     grid[row][col] == '0' or \
        #     (row, col) in visited:
        #         return

        #     visited.add((row, col))
        #     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        #     for rowDir, colDir in directions:
        #         newRow = row + rowDir
        #         newCol = col + colDir
        #         dfs(newRow, newCol)

        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == '1' and (row, col) not in visited:
        #             dfs(row, col)
        #             islands += 1

        # return islands




















        #---------------------------------------------------------
        # BFS Again
        # if not grid:
        #     return 0

        # rows, cols = len(grid), len(grid[0])
        # visited = set()
        # islands = 0

        # def bfs(row, col):
        #     q = collections.deque()
        #     q.append((row, col))
        #     visited.add((row, col))
        #     while q:
        #         curr = q.popleft()
        #         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        #         for rowDirection, colDirection in directions:
        #             newRow = curr[0] + rowDirection
        #             newCol = curr[1] + colDirection

        #             if newRow >= 0 and newCol >= 0 and \
        #             newRow < rows and newCol < cols and \
        #             grid[newRow][newCol] == '1' and \
        #             (newRow, newCol) not in visited:
        #                 q.append((newRow, newCol))
        #                 visited.add((newRow, newCol))

        # for row in range(rows):
        #     for col in range(cols):
        #         if (row, col) not in visited and grid[row][col] == '1':
        #             bfs(row, col)
        #             islands += 1

        # return islands
        #---------------------------------------------------------
        # BFS approach
        # if not grid:
        #     return 0
        # rows, cols = len(grid), len(grid[0])
        # islands = 0
        # visit = set()

        # def bfs(row, col):
        #     q = collections.deque()
        #     visit.add((row, col))
        #     q.append((row, col))

        #     while q:
        #         r, c = q.popleft()
        #         directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        #         for rdir, cdir in directions:
        #             newRow = r + rdir
        #             newCol = c + cdir
        #             if (newRow in range(rows) and
        #                 newCol in range(cols) and
        #                 grid[newRow][newCol] == "1" and
        #                 (newRow, newCol) not in visit):
        #                 q.append((newRow, newCol))
        #                 visit.add((newRow, newCol))
        
        # for row in range(rows):
        #     for col in range(cols):
        #         if grid[row][col] == "1" and (row, col) not in visit:
        #             bfs(row, col)
        #             islands += 1
        # return islands