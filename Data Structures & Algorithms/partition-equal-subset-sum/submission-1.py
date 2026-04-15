class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Top-down without memoization
        total_sum = sum(nums)
        if total_sum % 2:
            return False
        
        def canMakeSum(i, target):
            if i >= len(nums):
                return False
            if target == 0:
                return True
            if target < 0:
                return False
            
            # recursive case (include vs skip)
            include = canMakeSum(i + 1, target-nums[i])
            skip = canMakeSum(i+1, target)

            if include or skip:
                return True
            else:
                return False
        return canMakeSum(0, total_sum // 2)