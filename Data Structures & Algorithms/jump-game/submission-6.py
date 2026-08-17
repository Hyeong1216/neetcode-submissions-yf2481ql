class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #2. greedy
        furthest = 0
        for i in range(len(nums)):
            if i > furthest:
                return False
            furthest = max(furthest, i + nums[i])
            if furthest >= len(nums)-1:
                return True
        return True

        



# class Solution:
#     def canJump(self, nums: List[int]) -> bool:
#         #1. brute
#         def bt(index):
#             if index >= len(nums)-1:
#                 return True
#             if nums[index] == 0:
#                 return False
#             for jump_length in range(1, nums[index] + 1):
#                 next_index = index + jump_length
#                 if bt(next_index):
#                     return True
#             return False
        
#         return bt(0)
        