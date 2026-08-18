class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def bt(start, curr):
            res.append(curr[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                curr.append(nums[i])
                bt(i+1, curr)
                curr.pop()











        bt(0, [])
        return res














# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()
#         def bt(start, subset):
#             res.append(subset[:])

#             for i in range(start, len(nums)):
#                 if i > start and nums[i] == nums[i-1]:
#                     continue
                
#                 subset.append(nums[i])
#                 bt(i+1, subset)
#                 subset.pop()
    

#         bt(0, [])
#         return res