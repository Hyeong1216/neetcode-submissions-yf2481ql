class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # 0, 1, 2, 3, 4, 5, 6
        # 1, 2, 3, 4, 5, 6, 0
        # 2, 3, 4, 5, 6, 0, 1
        # 3, 4, 5, 6, 0, 1, 2
        # 4, 5, 6, 0, 1, 2, 3
        # 5, 6, 0, 1, 2, 3, 4
        # 6, 0, 1, 2, 3, 4, 5
        n = len(nums)
        total = float('-inf')
        for i in range(n):
            curr_total = 0
            for j in range(i, i + n):
                # print(f"j:{j}, n:{n}, j%n:{j%n}")
                curr_total += nums[j % n]
                total = max(total, curr_total)
            # print()

        return total


        