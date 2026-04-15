class Solution:
    def jump(self, nums: List[int]) -> int:
        # Bottom up
        n = len(nums)
        dp = [0] * n
        dp[n-1] = 0
        for i in range(n-2, -1, -1):
            dp[i] = float('inf')
            for jump_size in range(1, nums[i]+1):
                next_pos = jump_size + i
                if next_pos < n:
                    dp[i] = min(dp[i], 1 + dp[next_pos])
        
        return dp[0]
        #--------------------------------------------------
        # top down

        # memo = {}

        # def dfs(idx):
        #     # base case
        #     if idx == len(nums) - 1:
        #         return 0
            
        #     if idx in memo:
        #         return memo[idx]

        #     count = float('inf')
        #     for jump_size in range(1, nums[idx]+1):
        #         next_idx = idx + jump_size
        #         if next_idx < len(nums):
        #             count = min(count, dfs(next_idx) + 1)
            
        #     memo[idx] = count
        #     return count

        # return dfs(0)