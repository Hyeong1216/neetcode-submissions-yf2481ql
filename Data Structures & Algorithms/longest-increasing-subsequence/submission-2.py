class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 1. Brute Force: O(2^n) - each element has 2 choices (include/exclude)
        # def helper(index, prev_value):
        #     if index == len(nums):
        #         return 0

        #     # choice 1: skip the current element
        #     skip = helper(index + 1, prev_value)

        #     # choice 2: Include the current element (if possible)
        #     include = 0
        #     if prev_value < nums[index]:
        #         include = 1 + helper(index+1, nums[index])

        #     return max(skip, include)

        # return helper(0, float('-inf'))
        #----------------------------------------------------------------------
        # 2. Classic DP: O(n^2)
        # n = len(nums)
        # dp = [1] * n # Each element forms a subsequence of lenghth 1 by itself

        # for i in range(1, n):
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             dp[i] = max(dp[j] + 1, dp[i])

        # return max(dp)
        #----------------------------------------------------------------------
        # 3. Binary Search DP
        import bisect
        tails = []
        for num in nums:
            # Case 1: num can extend the longest subsequence
            if not tails or (tails[-1] < num):
                tails.append(num)

            # Case 2: num should replace some element
            else:
                # Find the position where num should replace an element
                # We want to find the leftmost position where tails[pos] >= num
                pos = bisect.bisect_left(tails, num)
                tails[pos] = num


        return len(tails)



            