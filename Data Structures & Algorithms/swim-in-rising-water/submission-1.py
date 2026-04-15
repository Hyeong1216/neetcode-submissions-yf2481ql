class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        # Binary search + BFS
        n = len(grid)

        def canReach(maxTime):
            # BFS to see if we can reach end with water level = maxTime
            if grid[0][0] > maxTime:
                return False
            
            queue = [(0, 0)]
            visited = set([(0, 0)])
            directions = [(0,1), (0,-1), (-1,0), (1,0)]
            while queue:
                row, col = queue.pop(0)
                if row == n-1 and col == n-1:
                    return True
                
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < n and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] <= maxTime):
                        visited.add((nr, nc))
                        queue.append((nr, nc))
            return False

        left, right = 0, max(max(row) for row in grid)
        while left < right:
            mid = (left + right) // 2
            if canReach(mid):
                right = mid
            else:
                left = mid + 1
        return left
        #---------------------------------------------
        # Brute Force DFS
        # rows, cols = len(grid), len(grid[0])
        # n = len(grid)
        # directions = [(0,1), (0,-1), (-1,0), (1,0)]

        # def dfs(row, col, visited, current_max):
        #     # Base case: reached bottom-right corner
        #     if row == n - 1 and col == n - 1:
        #         return max(current_max, grid[row][col])
        #     visited.add((row, col))
        #     current_max = max(current_max, grid[row][col])
        #     min_time = float('inf')

        #     for dr, dc in directions:
        #         new_row, new_col = dr + row, dc + col

        #         if (0 <= new_row < n and 0 <= new_col < n and (new_row, new_col) not in visited):
        #             path_max = dfs(new_row, new_col, visited, current_max)
        #             min_time = min(min_time, path_max)
            
        #     visited.remove((row, col))
        #     return min_time

        # return dfs(0, 0, set(), 0)

            
        
            