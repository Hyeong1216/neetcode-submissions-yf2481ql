class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1. Brute force: O(n^3)
        # max_sum = float('-inf')
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         max_sum = max(sum(nums[i:j+1]), max_sum)
        # return max_sum

        # 2. Brute force: O(n^2)
        # max_sum = float('-inf')
        # for i in range(len(nums)):
        #     current_sum = 0
        #     for j in range(i, len(nums)):
        #         print(f"i: {i}, j: {j}")
        #         current_sum += nums[j]
        #         max_sum = max(current_sum, max_sum)
        # return max_sum

        # 3. Kadane's algorithm
        max_sum = nums[0]
        current_sum = nums[0]
        for i in range(1, len(nums)):
            if (current_sum+nums[i]) < nums[i]:
                current_sum = nums[i]
            else:
                current_sum = current_sum + nums[i]
            max_sum = max(max_sum, current_sum)
        return max_sum

