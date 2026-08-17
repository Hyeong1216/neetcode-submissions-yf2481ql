class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 1. bottom up
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != float('inf') else -1













# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         # Solution
#         # 1. Can there be no answer for this
#         # 2. can input length be zero?

#         # Approaches
#         # 1. Bottom up
#         # create DP array
#         # dp = [float('inf')] * (amount + 1)
#         # dp[0] = 0 # base case: 0 coins for amount 0

#         # # Fill DP array from 1 to amount
#         # for i in range(1, amount + 1):
#         #     for coin in coins:
#         #         if coin <= i:
#         #             dp[i] = min(dp[i], dp[i-coin]+1)
#         # return dp[amount] if dp[amount] != float('inf') else -1


#         # 2. Top down memoization
#         if amount == 0:
#             return 0
#         memo = {}

#         def helper(remain):
#             if remain == 0:
#                 return 0
#             if remain < 0:
#                 return float('inf')
#             if remain in memo:
#                 return memo[remain]
            
#             min_coins = float('inf')
#             for coin in coins:
#                 if coin <= remain:
#                     result = helper(remain - coin)
#                     min_coins = min(min_coins, result + 1)
#             memo[remain] = min_coins
#             return min_coins
#         result = helper(amount)
#         return result if result != float('inf') else -1