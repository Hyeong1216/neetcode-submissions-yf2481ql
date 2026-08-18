class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def bt(start, curr, remain):
            if remain == 0:
                res.append(curr[:])
            if remain < 0:
                return
            for i in range(start, len(nums)):
                curr.append(nums[i])
                bt(i, curr, remain-nums[i])
                curr.pop()

        bt(0, [], target)
        return res














# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res = []

#         def bt(start, subset, remain):
#             if remain == 0:
#                 res.append(subset[:])
#                 return
#             elif remain < 0:
#                 return

#             for i in range(start, len(nums)):
#                 subset.append(nums[i])
#                 bt(i, subset, remain-nums[i])
#                 subset.pop()


#         bt(0, [], target)
#         return res

























# class Solution:
#     def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
#         res = []
#         def bt(start, subset, remain):
#             if remain == 0:
#                 res.append(subset[:])
#                 return

#             if remain < 0:
#                 return
            
#             for i in range(start, len(nums)):
#                 subset.append(nums[i])

#                 bt(i, subset, remain-nums[i])

#                 subset.pop()


#         bt(0, [], target)
#         return res