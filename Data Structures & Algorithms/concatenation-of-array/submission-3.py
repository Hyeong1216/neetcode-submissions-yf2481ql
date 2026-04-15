class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # res = []
        # for i in range(len(nums)):
        #     res.append(nums[i])

        # for i in range(len(nums)):
        #     res.append(nums[i])
        # return res
#-------------------------------------------------------------
        # res = []

        # for i in range(2):
        #     for num in nums:
        #         res.append(num)
        # return res
#-------------------------------------------------------------
        res = [0] * (2 * len(nums))
        for i in range(len(nums)):
            res[i] = res[i+len(nums)] = nums[i]
        return res