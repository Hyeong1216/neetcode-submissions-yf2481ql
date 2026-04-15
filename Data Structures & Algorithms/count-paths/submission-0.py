class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]

        # Base cases: what should we initialize?
        # Think about: how many ways to reach cells in first row and first column
        
        # First row: all cells have 1 way to reach
        for j in range(n):
            dp[0][j] = 1
        # First column: all cells have 1 way to reach
        for i in range(m):
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]