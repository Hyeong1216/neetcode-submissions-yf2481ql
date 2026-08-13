class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # DFS
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        total = 0

        def dfs(r, c):
            if grid[r][c] == "0":
                return

            if (r, c) not in visited:
                visited.add((r, c))
            
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0 <= nr and nr < rows and 0 <= nc and nc < cols and grid[nr][nc] == "1" and (nr, nc) not in visited:
                    dfs(nr, nc)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    dfs(row, col)
                    total += 1
        return total














































# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # Questions:
#         # 1. Can the grid be empty?
#         # 2. Are islands only connected horizontally/vertically, or diagonally too?
#         # 3. Can we modify the grid in place? → affects whether we use visited set or not

#         # Approach 1: DFS — O(R * C)
#         # if not grid: return 0
#         # rows, cols = len(grid), len(grid[0])
#         # visited = set()
#         # directions = [(0,1),(0,-1),(1,0),(-1,0)]

#         # def dfs(row, col):
#         #     if row < 0 or row >= rows or col < 0 or col >= cols or \
#         #        grid[row][col] == "0" or (row, col) in visited:
#         #         return
#         #     visited.add((row, col))
#         #     for r, c in directions:
#         #         dfs(row + r, col + c)

#         # count = 0
#         # for row in range(rows):
#         #     for col in range(cols):
#         #         if grid[row][col] == "1" and (row, col) not in visited:
#         #             dfs(row, col)
#         #             count += 1
#         # return count

#         # Approach 2: BFS — O(R * C)
#         if not grid:
#             return 0

#         rows, cols = len(grid), len(grid[0])
#         visited = set()
#         directions = [(0,1),(0,-1),(1,0),(-1,0)]

#         def bfs(row, col):
#             q = deque()
#             q.append((row, col))
#             visited.add((row, col))
#             while q:
#                 curr_row, curr_col = q.popleft()
#                 for r, c in directions:
#                     nr, nc = curr_row + r, curr_col + c
#                     if nr < 0 or nr >= rows or nc < 0 or nc >= cols or \
#                        grid[nr][nc] == "0" or (nr, nc) in visited:
#                         continue
#                     q.append((nr, nc))
#                     visited.add((nr, nc))

#         count = 0
#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col] == "1" and (row, col) not in visited:
#                     bfs(row, col)
#                     count += 1
#         return count

#         # Time: O(R * C) — each cell visited once (both DFS and BFS)
#         # Space: DFS O(R*C) call stack worst case
#         #        BFS O(min(R,C)) queue at most diagonal length