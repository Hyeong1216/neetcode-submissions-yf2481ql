class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Questions
        # 1. there are at least one element in the nums?
        # 2. can all element be negative?
        # 3. Are there any constraints on the array size?

        # Kadane's algorithm
        curr_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(num, curr_sum+num)
            max_sum = max(max_sum, curr_sum)
        return max_sum
        # Time: O(n), Space: O(1) — Kadane's, single pass
