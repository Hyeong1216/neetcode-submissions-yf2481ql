class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Top down
        memo = {}
        def helper(remaining, coin_idx):
            if remaining == 0:
                return 1
            if remaining < 0:
                return 0
            if coin_idx >= len(coins):
                return 0
            
            if (remaining, coin_idx) in memo:
                return memo[(remaining, coin_idx)]
            
            result = 0
            result += helper(remaining, coin_idx + 1)
            result += helper(remaining-coins[coin_idx], coin_idx)

            memo[(remaining, coin_idx)] = result
            return result

        return helper(amount, 0)
        #------------------------------------------------
        # Bottom up
        # dp = [0] * (amount + 1)
        # dp[0] = 1
        
        # for coin in coins:
        #     for i in range(1, amount+1):
        #         if i - coin >= 0:
        #             dp[i] += dp[i - coin]
        # return dp[amount]

