class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # two pointer
        nums.sort()
        # print(nums)

        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[i] + nums[l] + nums[r]
                if curr_sum == 0:
                    temp = [nums[i], nums[l], nums[r]]
                    res.append(temp)
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1


                elif curr_sum < 0:
                    l += 1
                else:
                    r -= 1
            
                
        return res
    









# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         # two pointer
#         nums.sort()
#         print(nums)
        
#         # bruteforce (too slow, TLE)
#         res = []
#         for i in range(len(nums)-2):
#             for j in range(i + 1, len(nums)-1):
#                 for k in range(j + 1, len(nums)):
#                     if nums[i] + nums[j] + nums[k] == 0:
#                         temp = [nums[i], nums[j], nums[k]]
#                         if temp not in res:
#                             res.append(temp)
#         return res






















# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         nums.sort()
#         res = []

#         for i in range(len(nums)-2):
#             if i > 0 and nums[i] == nums[i-1]:
#                 continue
#             l, r = i + 1, len(nums) - 1

#             while l < r:
#                 total = nums[i] + nums[l] + nums[r]
#                 if total == 0:
#                     res.append([nums[i], nums[l], nums[r]])
#                     while l < r and nums[l] == nums[l + 1]:
#                         l += 1
#                     while l < r and nums[r] == nums[r - 1]:
#                         r -= 1
#                     l += 1
#                     r -= 1
#                 elif total > 0:
#                     r -= 1
#                 else:
#                     l += 1





#         return res