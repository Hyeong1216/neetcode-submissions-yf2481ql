class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Questions
        # Can input nums be len == 0?

        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1