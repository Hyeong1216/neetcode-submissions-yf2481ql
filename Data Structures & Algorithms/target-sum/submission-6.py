class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Top down
        # memo = {}
        # def helper(index, current_sum):
        #     if index == len(nums):
        #         return 1 if current_sum == target else 0
            
        #     #memoization
        #     if (index, current_sum) in memo:
        #         return memo[(index, current_sum)]
            
        #     result = helper(index+1, current_sum+nums[index]) + helper(index+1, current_sum-nums[index])

        #     memo[(index, current_sum)] = result
        #     return result

        # return helper(0, 0)
        #--------------------------------
        #bottom up
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n+1)]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i+1][total+nums[i]] += count
                dp[i+1][total-nums[i]] += count
                
        return dp[n][target]
