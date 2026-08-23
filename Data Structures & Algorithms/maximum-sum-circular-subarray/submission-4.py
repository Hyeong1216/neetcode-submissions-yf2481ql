class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Optimized Kadane
        unwrapped_max = float('-inf')
        unwrapped_min = float('inf')
        curr = 0
        curr_min = 0
        total = 0
        for i in range(len(nums)):
            # curr_max
            curr = max(nums[i], curr + nums[i])
            unwrapped_max = max(unwrapped_max, curr)

            # curr_min
            curr_min = min(nums[i], curr_min+nums[i])
            unwrapped_min = min(curr_min, unwrapped_min)
        
            # total
            total += nums[i]
        # print(unwrapped_max)
        # print(unwrapped_min)


        wrap_max = total - unwrapped_min

        return max(wrap_max, unwrapped_max) if unwrapped_max >= 0 else unwrapped_max






        








# class Solution:
#     def maxSubarraySumCircular(self, nums: List[int]) -> int:
#         # brute force
#         n = len(nums)
#         total = float('-inf')
#         for i in range(n):
#             curr_total = 0
#             for j in range(i, i + n):
#                 curr_total += nums[j % n]
#                 total = max(total, curr_total)

#         return total


        