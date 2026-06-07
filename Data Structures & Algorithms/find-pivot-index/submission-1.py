class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Questions
        # Can input nums be len == 0?

        # Brute force
        # for i in range(len(nums)):
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i
        # return -1

        # O(N)
        total = sum(nums)
        leftSum = 0
        for i in range(len(nums)):
            leftSum += nums[i]
            if leftSum - nums[i] == total - leftSum:
                return i

        return -1