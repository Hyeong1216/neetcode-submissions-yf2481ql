class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        prev = 0
        for i in range(len(nums)):
            prev = nums[i] ^ prev
        return prev