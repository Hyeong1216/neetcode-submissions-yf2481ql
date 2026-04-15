class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1. Brute force: O(n^3)
        # max_sum = float('-inf')
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         max_sum = max(sum(nums[i:j+1]), max_sum)
        # return max_sum

        # 2. Brute force: O(n^2)
        max_sum = float('-inf')
        for i in range(len(nums)):
            current_sum = 0
            for j in range(i, len(nums)):
                current_sum += nums[j]
                max_sum = max(current_sum, max_sum)
        return max_sum
