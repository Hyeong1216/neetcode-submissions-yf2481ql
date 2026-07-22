class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Two pass
        # ans = []
        # for num in nums:
        #     ans.append(num)
        # for num in nums:
        #     ans.append(num)

        # return ans

        # one pass
        ans = [0] * (len(nums)*2)
        for i in range(len(nums)):
            ans[i] = ans[i+len(nums)] = nums[i]
        return ans
