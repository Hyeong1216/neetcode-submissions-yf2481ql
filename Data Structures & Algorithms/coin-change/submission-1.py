class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. Top down memoization
        
        # # base case
        # if amount == 0:
        #     return 0
        # memo = {}

        # def helper(remaining_amount):
        #     if remaining_amount == 0:
        #         return 0
            
        #     if remaining_amount < 0:
        #         return float('inf')
            
        #     if remaining_amount in memo:
        #         return memo[remaining_amount]
            
        #     min_coins = float('inf')

        #     for coin in coins:
        #         if coin <= remaining_amount:
        #             result = helper(remaining_amount - coin)
        #             min_coins = min(min_coins, result + 1)

        #     memo[remaining_amount] = min_coins
        #     return min_coins

        # result = helper(amount)

        # return result if result != float('inf') else - 1

        #----------------------------------------------------

        # 2. bottom up
        # create DP array
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0 # base case: 0 coins for amount 0

        # Fill DP array from 1 to amount
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin]+1)                    
        
        return dp[amount] if dp[amount] != float('inf') else -1

