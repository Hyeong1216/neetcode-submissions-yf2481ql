class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # bottom up
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0] * n for _ in range(n)]
        print(f"n:{n}")
        for length in range(3, n+1):
            for left in range(n - length + 1):
                right = left + length - 1

                print(f"left:{left} - right:{right} - length:{length}")
                for k in range(left + 1, right):
                    # TODO: Calculate coins for bursting k last
                    coins = nums[left] * nums[k] * nums[right]

                    # TODO: Add coins from left and right subproblems
                    coins += dp[left][k]
                    coins += dp[k][right]

                    # TODO: Update dp[left][right] with maximum
                    dp[left][right] = max(dp[left][right], coins)
                    




        return dp[0][n-1] # returning the result of entire range