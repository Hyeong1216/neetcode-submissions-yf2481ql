class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Bottom up
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        target = total_sum // 2
        
        # dp[j] = True if we can make sum j
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            #Update dp array to include new possible sums
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]




        return dp[target]







        #------------------------------------------

        # # Top-down without memoization
        # total_sum = sum(nums)
        # if total_sum % 2:
        #     return False
        
        # def canMakeSum(i, target):
        #     if i >= len(nums):
        #         return False
        #     if target == 0:
        #         return True
        #     if target < 0:
        #         return False
            
        #     # recursive case (include vs skip)
        #     include = canMakeSum(i + 1, target-nums[i])
        #     skip = canMakeSum(i+1, target)

        #     return include or skip
        # return canMakeSum(0, total_sum // 2)
        #------------------------------------------
        # Top-down with memoization
        # total_sum = sum(nums)
        # if total_sum % 2:
        #     return False
        # memo = {}
        # def canMakeSum(i, target):
        #     if i >= len(nums):
        #         return False
        #     if target == 0:
        #         return True
        #     if target < 0:
        #         return False
        #     if (i, target) in memo:
        #         return memo[(i, target)]
            
        #     # recursive case (include vs skip)
        #     include = canMakeSum(i + 1, target-nums[i])
        #     skip = canMakeSum(i+1, target)

        #     memo[(i, target)] = include or skip

        #     return memo[(i, target)]
        # return canMakeSum(0, total_sum // 2)

