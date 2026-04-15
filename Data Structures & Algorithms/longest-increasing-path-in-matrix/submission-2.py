class Solution:
    def longestIncreasingPath(self, mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        memo = {}
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        max_len = 0
        def dfs(row, col):
            if (row, col) in memo:
                return memo[(row, col)]
            
            length = 1
            temp = 0
            for dr, dc in directions:
                nr, nc = dr+row, dc+col
                if 0 <= nr < rows and 0 <= nc < cols and mat[nr][nc] > mat[row][col]:
                    temp = max(temp, dfs(nr, nc))
            
            length += temp
            memo[(row, col)] = length
            return length

        for row in range(rows):
            for col in range(cols):
                max_len = max(max_len, dfs(row, col))
        return max_len