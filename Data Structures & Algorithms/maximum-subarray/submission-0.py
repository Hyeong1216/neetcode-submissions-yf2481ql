class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1. Brute force: O(n^3)
        max_sum = float('-inf')
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                max_sum = max(sum(nums[i:j+1]), max_sum)
        return max_sum
