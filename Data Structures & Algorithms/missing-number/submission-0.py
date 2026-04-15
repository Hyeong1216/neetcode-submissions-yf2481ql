class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n #3
        for i in range(n):
            xorr ^= nums[i] ^ i
        return xorr