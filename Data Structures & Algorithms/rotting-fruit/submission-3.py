class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1
        
        q = collections.deque()
        rows, cols = len(grid), len(grid[0])

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    q.append((row, col))
        total_time = 0
        while q:
            level_size = len(q)
            has_new_rotten = False

            for _ in range(level_size):
                curr_row, curr_col = q.popleft()
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
                
                for row_dir, col_dir in directions:
                    new_row = curr_row + row_dir
                    new_col = curr_col + col_dir

                    if new_row >= 0 and new_row < rows and \
                    new_col >= 0 and new_col < cols and \
                    grid[new_row][new_col] == 1:
                        has_new_rotten = True
                        grid[new_row][new_col] = 2
                        q.append((new_row, new_col))

            if has_new_rotten:
                total_time += 1
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    return -1

        return total_time