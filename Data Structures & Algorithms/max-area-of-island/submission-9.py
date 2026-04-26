class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # bfs
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            visited.add((row, col))
            temp_area = 0
            while q:
                temp_area += 1
                curr_row, curr_col = q.popleft()
                for rowDir, colDir in directions:
                    nr, nc = curr_row+rowDir, curr_col+colDir
                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited or grid[nr][nc] == 0:
                        continue
                    q.append((nr, nc))
                    visited.add((nr,nc))
            
            return temp_area
                    


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(max_area, bfs(row, col))

        return max_area

        

# #-----------
# class Solution:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         # BFS
#         if not grid:
#             return 0
#         rows, cols = len(grid), len(grid[0])
#         visited = set()
#         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#         def bfs(row, col):
#             q = deque()
#             q.append((row, col))
#             visited.add((row, col))

#             while q:
#                 curr_row, curr_col = q.popleft()
#                 for rowDir, colDir in directions:
#                     nr, nc = curr_row + rowDir, curr_col + colDir
#                     if nr < 0 or nr >= rows or nc < 0 or nc >= cols or (nr, nc) in visited or grid[nr][nc] == "0":
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
#         #-------------------------------------------------
#         #DFS
#         if not grid:
#             return 0
#         visited = set()
#         rows, cols = len(grid), len(grid[0])
#         count = 0
#         directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#         def dfs(row, col):
#             if row < 0 or row >= rows or col < 0 or col >= cols or (row, col) in visited or grid[row][col] == "0":
#                 return
#             visited.add((row, col))
#             for rowDir, colDir in directions:
#                 nr, nc = row+rowDir, col+colDir
#                 dfs(nr, nc)




#         for row in range(rows):
#             for col in range(cols):
#                 if grid[row][col] == "1" and (row, col) not in visited:
#                     dfs(row, col)
#                     count += 1

#         return count 
