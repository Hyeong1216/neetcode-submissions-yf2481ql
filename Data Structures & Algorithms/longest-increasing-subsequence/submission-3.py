class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Questions:
        # 1. Can input list be empty?

        # Key insight: dp[i] = length of LIS ending at index i
        # For each i, check all j < i where nums[j] < nums[i]
        # dp[i] = max(dp[j] + 1) for all valid j

        # Approach 1: Bottom-up DP — O(N²) time, O(N) space
        n = len(nums)
        dp = [1] * n  # each element forms subsequence of length 1 by itself

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)

        # Approach 2: Binary Search optimized — O(N log N) time, O(N) space
        # tails = []
        # for num in nums:
        #     lo, hi = 0, len(tails)
        #     while lo < hi:
        #         mid = (lo + hi) // 2
        #         if tails[mid] < num:
        #             lo = mid + 1
        #         else:
        #             hi = mid
        #     if lo == len(tails):
        #         tails.append(num)
        #     else:
        #         tails[lo] = num
        # return len(tails)

        # Time: O(N²) DP / O(N log N) binary search
        # Space: O(N)